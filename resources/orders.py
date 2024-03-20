from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
# from flask_jwt_extended import jwt_required

from models import db, Order
from schemas import  order_schema, orders_schema

class Order_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('customer_id', required=True, help="customer_id is required")
    parser.add_argument('product_id', required=True, help="product_id is required")
    # parser.add_argument('Order_employees', required=True, help="Order_employees is required")

    def get(self):
        Orders = Order.query.all()

        response = make_response(
            orders_schema.dump(Orders),
            200,
        )

        return response
    
    def post(self):
        data = Order_list.parser.parse_args()
        new_Order = Order(**data)

        db.session.add(new_Order)
        db.session.commit()

        response = make_response(
            order_schema.dump(new_Order),
            201
        )

        return response
    
class Order_by_id(Resource):
    def get(self, id):
        getOrder = Order.query.filter_by(id=id).first()
        
        if getOrder == None:
            response_body = {
                "error": "Order does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                order_schema.dump(getOrder),
                200,
            )

            return response
    
    def patch(self,id):
        newOrder = Order.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(Order, attr, request.get_json().get(attr))

        db.session.add(newOrder)
        db.session.commit()


        response = make_response(
            order_schema.dump(newOrder),
            201
        )

        return response
    
    def delete(self,id):
        getOrder = Order.query.filter_by(id=id).first()
        db.session.delete(getOrder)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Order data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response