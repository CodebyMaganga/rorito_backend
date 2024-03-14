from flask_restful import Resource, reqparse
from flask import make_response,jsonify ,request
from flask_bcrypt import Bcrypt,generate_password_hash
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity


from models import db, Admin
from schemas import  admin_schema, admins_schema

bcrypt = Bcrypt()

jwt = JWTManager()

class Admin_SignUp(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', required=True, help="first_name is required")
    parser.add_argument('last_name', required=True, help="last_name is required")
    parser.add_argument('email', required=True, help="email is required")
    parser.add_argument('password', required=True, help="password is required")


    def get(self):
        admins= Admin.query.all()

        response = make_response(
            admins_schema.dump(admins),
            200,
        )

        return response
    
    def post(self):
        data = Admin_SignUp.parser.parse_args()
        new_admin = Admin(**data)

        if not new_admin.email or not new_admin.password:
            return {'message': 'Both email and password are required'}, 400

        # Check if the email is already registered
        if Admin.query.filter_by(email = new_admin.email).first():
            return {'message': 'Admin already registered'}, 400

        new_admin.password = generate_password_hash(new_admin.password).decode('utf-8')
        db.session.add(new_admin)
        db.session.commit()

        return ({'message': 'Admin registered successfully'}), 201
    
class Admin_Login(Resource):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True, help="Email address is required")
        parser.add_argument('password', required=True, help="Password is required")
        
        def post(self):
            data = Admin_Login.parser.parse_args()

            
            getadmin = Admin.query.filter_by(email= data['email']).first()

            if getadmin:
                    password_is_correct= getadmin.check_password(data['password'])

                    if password_is_correct:
                        #check these incase of any problem
                        admin_json = admin_schema.dump(getadmin)
                        access_token = create_access_token(identity=admin_json['id'])
                        refresh_token = create_refresh_token(identity=admin_json['id'])
                        return {"message": "Login successful",
                                "status": "success",
                                "access_token": access_token,
                                "refresh_token": refresh_token,
                                "user": admin_json,
                                }, 200
                    else:
                        return {'message': 'Invalid email or password'}, 401
            else:
                    return {'message': 'Admin not found'}, 404


class Admin_list(Resource):

    def get(self):
        admins = Admin.query.all()

        response = make_response(
            admins_schema.dump(admins),
            200,
        )

        return response
    


class Admin_by_id(Resource):
    def get(self, id):
        admin = Admin.query.filter_by(id=id).first()
        
        if admin == None:
            response_body = {
                "error": "admin does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response

        else:
            response = make_response(
                admin_schema.dump(admin),
                200,
            )

            return response
    
    def patch(self,id):
        admin = Admin.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(admin, attr, request.get_json().get(attr))

        db.session.add(admin)
        db.session.commit()


        response = make_response(
            admin_schema.dump(admin),
            201
        )

        return response
    
    def delete(self,id):
        admin = Admin.query.filter_by(id=id).first()
        db.session.delete(admin)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "admin data deleted successfully."    
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response



