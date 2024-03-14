from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
# from flask_jwt_extended import jwt_required

from models import db, Cart_Item
from schemas import  cart_item_schema, cart_items_schema

class Cart_Item_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Cart_Item_name', required=True, help="Cart_Item_name is required")
    # parser.add_argument('Cart_Item_employees', required=True, help="Cart_Item_employees is required")

    def get(self):
        Cart_Items = Cart_Item.query.all()

        response = make_response(
            cart_items_schema.dump(Cart_Items),
            200,
        )

        return response
    
    def post(self):
        data = Cart_Item_list.parser.parse_args()
        new_Cart_Item = Cart_Item(**data)

        db.session.add(new_Cart_Item)
        db.session.commit()

        response = make_response(
            cart_item_schema.dump(new_Cart_Item),
            201
        )

        return response
    
class Cart_Item_by_id(Resource):
    def get(self, id):
        getCartItem = Cart_Item.query.filter_by(id=id).first()
        
        if getCartItem == None:
            response_body = {
                "error": "Cart_Item does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                cart_item_schema.dump(getCartItem),
                200,
            )

            return response
    
    def patch(self,id):
        newCartItem = Cart_Item.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(Cart_Item, attr, request.get_json().get(attr))

        db.session.add(newCartItem)
        db.session.commit()


        response = make_response(
            cart_item_schema.dump(newCartItem),
            201
        )

        return response
    
    def delete(self,id):
        getCart_Item = Cart_Item.query.filter_by(id=id).first()
        db.session.delete(getCart_Item)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Cart_Item data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response