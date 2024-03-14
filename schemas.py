from flask_marshmallow import Marshmallow
from marshmallow import fields
from models import Admin, Product, Customer, Order, Cart_Item

ma = Marshmallow()

class AdminSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Admin
        load_instance = True

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor("admin_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("admin_list"),
        }
    )

admin_schema = AdminSchema()
admins_schema = AdminSchema(many=True)

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor("product_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("product_list"),
        }
    )

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        load_instance = True
        fields = ('id', "first_name", "last_name", "phone_number", "email", "gender")

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor("customer_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("customer_list"),
        }
    )

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        include_fk = True
    
    customer_id = ma.Int()
    customer_details = fields.Method("get_customer_details")

    product_id = ma.Int()
    product_details = fields.Method("get_product_details")
    
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor("order_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("order_list"),
        }
    )

    def get_customer_details(self, obj):
        customer = Customer.query.get(obj.customer_id)
        if customer:
            return {
                
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "phone_number": customer.phone_number,
                "email": customer.email,
                
            }
        return None
    
    def get_product_details(self, obj):
        product = Product.query.get(obj.customer_id)
        if product:
            return {
                
                "name": product.name,
                "brand": product.brand,
                "price": product.price,

                
            }
        return None

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

class CartItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cart_Item
        load_instance = True
        include_fk = True

    customer_id = ma.Int()
    customer_details = fields.Method("get_customer_details")

    product_id = ma.Int()
    product_details = fields.Method("get_product_details")
    
    def get_customer_details(self, obj):
        customer = Customer.query.get(obj.customer_id)
        if customer:
            return {
                
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "phone_number": customer.phone_number,
                "email": customer.email,
                
            }
        return None
    
    def get_product_details(self, obj):
        product = Product.query.get(obj.customer_id)
        if product:
            return {
                
                "name": product.name,
                "brand": product.brand,
                "price": product.price,

                
            }
        return None



    url = ma.Hyperlinks(
        {
            "self": ma.URLFor("cart_item_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("cart_item_list"),
        }
    )

cart_item_schema = CartItemSchema()
cart_items_schema = CartItemSchema(many=True)
