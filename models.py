from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from flask_bcrypt import check_password_hash


db = SQLAlchemy()

class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique = True, nullable=False)
    password = db.Column(db.String,nullable=False)

    def check_password(self,plain_password):
        return check_password_hash(self.password,plain_password)

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String,nullable=False)
    url = db.Column(db.String, nullable=False)

class Customer(db.Model):
    __tablename__='customers'

    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, unique = True,nullable=False)
    email = db.Column(db.String, unique = True, nullable=False)
    password = db.Column(db.String,nullable=False)

    def check_password(self,plain_password):
        return check_password_hash(self.password,plain_password)



class Order(db.Model): 
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id') )
    time_ordered = db.Column(db.DateTime, default=datetime.utcnow)

    ordered_products = db.relationship('Product', backref='orders')
    ordered_customers = db.relationship('Customer', backref='orders')  


class Cart_Item(db.Model):
    __tablename__ = 'cartitems'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id') )

    cart_products = db.relationship('Product', backref='cart_items')
    cart_customers = db.relationship('Customer', backref='cart_items')  





