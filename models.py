from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from flask_bcrypt import check_password_hash


db = SQLAlchemy()

orders_products_association = db.Table('orders_products',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)

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
    image_url = db.Column(db.String, nullable=False)

    orders = db.relationship('Order', secondary=orders_products_association, back_populates='products')

class Customer(db.Model):
    __tablename__='customers'

    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String,nullable=False)
    delivery_details = db.Column(db.String) 



class Order(db.Model): 
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    time_ordered = db.Column(db.DateTime, default=datetime.utcnow)

    # Define the many-to-many relationship with Product via the association table
    products = db.relationship('Product', secondary=orders_products_association,
                               primaryjoin=id == orders_products_association.c.order_id,
                               secondaryjoin=Product.id == orders_products_association.c.product_id,
                               back_populates='orders')
    
    # Define the relationship with Customer
    ordered_customer = db.relationship('Customer', backref='orders')

    def serialize_time_ordered(self):
        return self.time_ordered.strftime("%Y-%m-%d %H:%M:%S")  

class Cart_Item(db.Model):
    __tablename__ = 'cartitems'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id') )

    cart_products = db.relationship('Product', backref='cart_items')
    cart_customers = db.relationship('Customer', backref='cart_items')  





