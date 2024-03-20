from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_bcrypt import Bcrypt,generate_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity


from models import db, Customer, Order, Product
from schemas import  customer_schema, customers_schema

bcrypt = Bcrypt()

jwt = JWTManager()


class Customer_list(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('Customer_name', required=True, help="Customer_name is required")
    # parser.add_argument('Customer_employees', required=True, help="Customer_employees is required")

    def get(self):
        Customers = Customer.query.all()

        response = make_response(
            customers_schema.dump(Customers),
            200,
        )

        return response
    
    def post(self):
        data = Customer_list.parser.parse_args()
        new_Customer = Customer(**data)

        db.session.add(new_Customer)
        db.session.commit()

        response = make_response(
            customer_schema.dump(new_Customer),
            201
        )

        return response
    
class Customer_by_id(Resource):
    def get(self, id):
        getCustomer = Customer.query.filter_by(id=id).first()
        
        if getCustomer == None:
            response_body = {
                "error": "Customer does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                customer_schema.dump(getCustomer),
                200,
            )

            return response
    
    def patch(self,id):
        newCustomer = Customer.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(Customer, attr, request.get_json().get(attr))

        db.session.add(newCustomer)
        db.session.commit()


        response = make_response(
            customer_schema.dump(newCustomer),
            201
        )

        return response
    
    def delete(self,id):
        getCustomer = Customer.query.filter_by(id=id).first()
        db.session.delete(getCustomer)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "Customer data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response




class Customer_SignUp(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', required=True, help="first_name is required")
    parser.add_argument('last_name', required=True, help="last_name is required")
    
    parser.add_argument('phone_number', required=True, help="phone_number is required")
    parser.add_argument('delivery_details', required=True, help="delivery details is required")
  


    def get(self):
        Customers= Customer.query.all()

        response = make_response(
            customers_schema.dump(Customers),
            200,
        )

        return response
    
    def post(self):
        data = Customer_SignUp.parser.parse_args()
        new_Customer = Customer(**data)

        # if not new_Customer.email or not new_Customer.password:
        #     return {'message': 'Both email and password are required'}, 400

        # # Check if the email is already registered
        # if Customer.query.filter_by(email = new_Customer.email).first():
        #     return {'message': 'Customer already registered'}, 400

        new_Customer.password = generate_password_hash(new_Customer.password).decode('utf-8')
        db.session.add(new_Customer)
        db.session.commit()

        return ({'message': 'Customer registered successfully'}), 201
    
class Customer_Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help="Email address is required")
    parser.add_argument('password', required=True, help="Password is required")

    def post(self):
        data = Customer_Login.parser.parse_args()

        getCustomer = Customer.query.filter_by(email=data['email']).first()

        if getCustomer:
            password_is_correct = getCustomer.check_password(data['password'])

            if password_is_correct:
                customer_json = customer_schema.dump(getCustomer)
                access_token = create_access_token(identity=customer_json['id'])
                refresh_token = create_refresh_token(identity=customer_json['id'])
                return {
                    "message": "Login successful",
                    "status": "success",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user": customer_json,
                }, 200
            else:
                return {'message': 'Invalid email or password'}, 401
        else:
            return {'message': 'Customer not found'}, 404
        
class CustomerOrder(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', required=True, help="first_name is required")
    parser.add_argument('last_name', required=True, help="last_name is required")
    parser.add_argument('phone_number', required=True, help="phone_number is required")
    parser.add_argument('delivery_details', required=True, help="delivery details is required")
    parser.add_argument('products', type=dict, action='append', required=True,
                        help="products is required and must be a list of dictionaries")

    def post(self):
        try:
            data = CustomerOrder.parser.parse_args()
        except ValueError as e:
            return {'message': str(e)}, 400

        # Extract customer data
        customer_data = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'phone_number': data['phone_number'],
            'delivery_details': data['delivery_details']
        }

        # Extract order data
        products = data['products']

        try:
            # Create customer
            new_customer = Customer(**customer_data)
            db.session.add(new_customer)
            db.session.commit()

            # Create orders
            for product_data in products:
                product_id = product_data.get('product_id')

                # Get product object from database
                product = Product.query.get(product_id)

                if product:
                    # Create a new order for each product
                    new_order = Order(customer_id=new_customer.id)
                    new_order.products.append(product)
                    db.session.add(new_order)
                else:
                    # Handle case where product is not found
                    return {'message': f'Product with ID {product_id} not found'}, 404
            
            db.session.commit()  # Commit all orders after the loop
            return {'message': 'Order placed successfully'}, 201
        except Exception as e:
            # Handle any errors gracefully
            db.session.rollback()
            return {'message': str(e)}, 500
