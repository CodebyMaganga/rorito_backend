from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
# from flask_jwt_extended import jwt_required

from models import db, Product
from schemas import  product_schema, products_schema

class Product_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('Product_name', required=True, help="Product_name is required")
    # parser.add_argument('Product_employees', required=True, help="Customer_employees is required")

    def get(self):
        Products = Product.query.all()

        response = make_response(
            products_schema.dump(Products),
            200,
        )

        return response
    
    def post(self):
        data = Product_list.parser.parse_args()
        new_Product = Product(**data)

        db.session.add(new_Product)
        db.session.commit()

        response = make_response(
            product_schema.dump(new_Product),
            201
        )

        return response
    
class Product_by_id(Resource):
    def get(self, id):
        getProduct = Product.query.filter_by(id=id).first()
        
        if getProduct == None:
            response_body = {
                "error": "Product does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                product_schema.dump(getProduct),
                200,
            )

            return response
    
    def patch(self,id):
        newProduct = Product.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(Product, attr, request.get_json().get(attr))

        db.session.add(newProduct)
        db.session.commit()


        response = make_response(
            product_schema.dump(newProduct),
            201
        )

        return response
    
    def delete(self,id):
        getProduct = Product.query.filter_by(id=id).first()
        db.session.delete(getProduct)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Product data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response