from flask import Flask
from flask_migrate import Migrate
from flask_restful  import Api
from models import db
from schemas import ma
from datetime import timedelta
from resources.products import Product_list, Product_by_id
from resources.customers import Customer_list,Customer_by_id,Customer_Login,Customer_SignUp
from resources.orders import Order_list, Order_by_id
from resources.cartItems import Cart_Item_list, Cart_Item_by_id
from resources.admins import Admin_list, Admin_by_id, Admin_Login, Admin_SignUp, jwt, bcrypt


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rorito.db'
# os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)


migrate =  Migrate(app, db)




db.init_app(app)
ma.init_app(app)

api=Api(app)

bcrypt.init_app(app)
jwt.init_app(app)

@app.route("/")
def index():
    return "<p>Code Check,One two</p>"

api.add_resource(Admin_SignUp, '/signUpAdmin')
api.add_resource(Admin_Login, '/loginAdmin')

api.add_resource(Customer_SignUp, '/signUpCustomer')
api.add_resource(Customer_Login, '/loginCustomer')

api.add_resource(Admin_list,'/admins')
api.add_resource(Admin_by_id,'/admins/<int:id>')

api.add_resource(Product_list,'/products')
api.add_resource(Product_by_id,'/products/<int:id>')

api.add_resource(Customer_list,'/customers')
api.add_resource(Customer_by_id,'/customers/<int:id>')

api.add_resource(Cart_Item_list,'/cartItems')
api.add_resource(Cart_Item_by_id,'/cartItems/<int:id>')

api.add_resource(Order_list,'/orders')
api.add_resource(Order_by_id,'/orders/<int:id>')


if __name__ == '__main__':
    app.run(port=5555,debug=True)