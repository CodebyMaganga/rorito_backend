from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth
import base64
from flask_migrate import Migrate
from flask_restful  import Api
from models import db
from schemas import ma
from datetime import timedelta, datetime
from resources.products import Product_list, Product_by_id
from resources.customers import Customer_list,Customer_by_id,Customer_Login,Customer_SignUp, CustomerOrder
from resources.orders import Order_list, Order_by_id
from resources.cartItems import Cart_Item_list, Cart_Item_by_id
from resources.admins import Admin_list, Admin_by_id, Admin_Login, Admin_SignUp, jwt, bcrypt
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rorito.db'
# os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

CONSUMER_KEY = 'hirVGHfjpI67nhxefvhC2t9EEHpdb1tJ6nOVz1O9kuT7IENE'
CONSUMER_SECRET = 'rYheTMyMDrKNJGPATKGeuNSjDBsVzNNtCoClDAseRcQ8UTGwo6w4O11oGpAl5PvN'

API_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

LIPA_NA_MPESA_ENDPOINT = 'https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query'

migrate =  Migrate(app, db)




db.init_app(app)
ma.init_app(app)

api=Api(app)

bcrypt.init_app(app)
jwt.init_app(app)

CORS(app)

@app.route("/")
def index():
    return "<p>Code Check,One two</p>"

api.add_resource(Admin_SignUp, '/signUpAdmin')
api.add_resource(Admin_Login, '/loginAdmin')

api.add_resource(Customer_SignUp, '/signUpCustomer')
api.add_resource(Customer_Login, '/loginCustomer')
api.add_resource(CustomerOrder, '/customer-order')

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

@app.route('/lipa-na-mpesa-payment', methods=['POST'])
def lipa_na_mpesa_payment():
    Timestamp = datetime.now()
    times = Timestamp.strftime('%Y%m%d%H%M%S')
    password = '174379' + 'MqDOj4RRK1qTNbFGI12pAo1gaNQ5lTuFW4CL1rB7Z/SRQWfW/jrwiDx0qilmEKShhX3dcJioIbBanoMpyd673yc2Bftq3Z3fhvLZZpWgd0BmMo/5gigzwk6ZfDuAXli5fEJEJY4HI0xq13dLSzNkP+NVJ+IPB2jMbOdTchX5KS/r5o/tt6I8HqjRdSB4b9hYrwLOyylQThVqm9EwqqSdI1jrKUzdSlzLB1hQzeyV2qWP3eGcur0H9lWKvCHzQ3trasx8Db21KO5B46O8tgLZKMoEcDUX+trcJhO+qVFF6yA1fjZlP0GPesGPBVfuyP1nKw856P/chEQW8cQDADyJsQ==' + times
    password = password = base64.b64encode(password.encode('utf-8')).decode('utf-8')

   
    try:
        # Extract order data from request
        order_data = request.json

        access_token = getAccessToken()
        
        # Construct request headers
        headers = {
            'Authorization': 'Bearer %s' % access_token,
            'Content-Type': 'application/json'
        }
        
        # Construct request payload
        payload = {
            'BusinessShortCode': '788485',
            'Password': password,  # You need to generate this password according to M-Pesa documentation
            'Timestamp': times,
            'TransactionType': 'CustomerBuyGoodsOnline',
            'Amount': '5',
            'PartyA': '0707849963',  # Customer phone number
            'PartyB': '174379',
            'PhoneNumber': '0707849963',  # Customer phone number
            'CallBackURL': 'https://09d7-41-90-181-160.ngrok-free.app/mpesa-callback',
            'AccountReference': 'Test',
            'TransactionDesc': 'Test'
        }
        
        # Make the request to Lipa na M-Pesa endpoint
        response = requests.post(f'{API_URL}{LIPA_NA_MPESA_ENDPOINT}', headers=headers, json=payload)

        if response.status_code == 200:
            # Payment initiated successfully
            return response.json()
        else:
            # Payment initiation failed
            return jsonify({'status': 'error', 'message': 'Failed to initiate payment'}), response.status_code
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/mpesa-callback', methods=['POST'])
def mpesa_callback():
    # Handle M-Pesa callback
    data = request.json
    print(data)
      # or request.form, depending on how M-Pesa sends the data
    # Process the callback data and update your application's state or database
    # Return a response to acknowledge receipt of the callback (optional)
    return jsonify({'status': 'success'}), 200


def getAccessToken():
    r = requests.get(API_URL,auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET))

    data = r.json()

    return data['access_token']

if __name__ == '__main__':
    app.run(port=5555,debug=True)