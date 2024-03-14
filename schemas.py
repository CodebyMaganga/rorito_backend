from flask_marshmallow import Marshmallow
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

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor("order_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("order_list"),
        }
    )

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

class CartItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cart_Item
        load_instance = True
        include_fk = True

    url = ma.Hyperlinks(
        {
            "self": ma.URLFor("cartItem_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("cartItem_list"),
        }
    )

cart_item_schema = CartItemSchema()
cart_items_schema = CartItemSchema(many=True)
