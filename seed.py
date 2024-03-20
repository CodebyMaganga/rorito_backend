from models import db, Admin, Product, Customer, Order, Cart_Item
from datetime import datetime
from app import app

with app.app_context():
    # # Create sample data for Admins
    # admin1 = Admin(id='admin1', first_name='Admin', last_name='One', email='admin1@example.com', password='password1')
    # admin2 = Admin(id='admin2', first_name='Admin', last_name='Two', email='admin2@example.com', password='password2')

    # Create sample data for Products
    
    product3 = Product(name='Taifa 13kg refill', brand='Taifa', price=3500, category='Gas', image_url='https://qleen2gas.co.ke/public/uploads/all/GY6XS5E13Qgnrm7Cg0kqvS8RHTFJzfQw3ZaFBzCq.png')
    product4 = Product(name='Total 13kg refill', brand='Total', price=5500, category='Gas', image_url='https://i0.wp.com/mamagas.co.ke/wp-content/uploads/2022/10/total-13kg-200x200-1.jpg?fit=620%2C620&ssl=1')
    product5 = Product(name='ProGas 6kg refill', brand='ProGas', price=1800, category='Gas', image_url='https://www.patabay.co.ke/wp-content/uploads/2020/05/progas-6kg-500x500.jpg')
    product6 = Product(name='ProGas 13kg refill', brand='ProGas', price=3300, category='Gas', image_url='https://i.roamcdn.net/hz/pi/base/ccc927d7d2979a38e4f26c8dac53932b/-/horizon-files-prod/pi/picture/q9rxmr8/60c7594d8837af528064ce0097f318898ea97778.jpeg')
    product7 = Product(name='SeaGas 13kg refill', brand='SeaGas', price=3400, category='Gas', image_url='https://atana.co.ke/wp-content/uploads/2020/03/sea-gas-13kgs.jpg')
    product8 = Product(name='SeaGas 6kg refill', brand='SeaGas', price=1300, category='Gas', image_url='https://www.gobeba.com/wp-content/uploads/2020/07/seagas-6kg-200x223.jpg')
    product9 = Product(name='Kinangop 500mlMilk', brand='Kinangop', price=50, category='Whole Milk', image_url='https://cdnprod.mafretailproxy.com/sys-master-root/hdb/h67/17328666017822/55457_main.jpg_480Wx480H')
    product10 = Product(name='kGas 13kg refill', brand='kGas', price=4500, category='Gas', image_url='https://maloogas.co.ke/wp-content/uploads/2022/06/kgas.png')
    product11 = Product(name='20L Refill', brand='Purified Water', price=100, category='Water', image_url='https://images-na.ssl-images-amazon.com/images/I/41c%2BX0dt04L._SY450_.jpg')
    product12 = Product(name='10L Refill', brand='Purified Water', price=50, category='Water', image_url='https://store.quality.mu/wp-content/uploads/2020/06/10l_web.jpg')
    product13 = Product(name='1l 24Pieces', brand='Purified Water', price=1200, category='Water', image_url='https://i5.walmartimages.com/asr/ad640e6b-c5b3-447e-bbc5-08468341a404.c161c5c5c464ff340f8340ac171b331a.jpeg?odnWidth=1000&odnHeight=1000&odnBg=ffffff')
    product14 = Product(name='500ml 24Pieces', brand='Purified Water', price=700, category='Water', image_url='https://bookacan.com/wp-content/uploads/2016/05/aquafina_500ml_mineral_water_bottle.jpg')
    product15 = Product(name='Dutch Lady', brand='DutchLady', price=80, category='Condensed Milk', image_url='https://images.yaoota.com/BzFYz9_mUcmBbykiyRNa0PRsdPg=/trim/yaootaweb-production-ke/media/crawledproductimages/ebc43ab830eb79dca7af5f4879c3203e60a16ee6.jpg')
    product16 = Product(name='Luna', brand='Luna', price=100, category='Condensed Milk', image_url='https://bestbuyltd.com/wp-content/uploads/2020/02/luna-condensed-sweet.jpg')
    product17 = Product(name='Magnolia', brand='Magnolia', price=120, category='Evaporated Milk', image_url='https://images.freshop.com/00652729106107/0c00c55e79345cb76c9a6ea1da677587_large.png')
    product18 = Product(name='Brookside milk powder', brand='Brookside', price=120, category='Milk Powder', image_url='https://cdnprod.mafretailproxy.com/sys-master-root/h50/h19/17130700865566/156431_main.jpg_480Wx480H')
    product19 = Product(name='Aptil Infant Milk', brand='Aptil', price=120, category='Infant Milk', image_url='https://portalpharmacy.ke/image/catalog/Aptamil/2.jpg')
    product20 = Product(name='13kg Regulator', brand='Regulator', price=800, category='Regulator', image_url='https://www.rectorygassupplies.co.uk/wp-content/uploads/2016/12/RCO27P.jpg')
    product21 = Product(name='6kg Regulator', brand='Regulator', price=500, category='Regulator', image_url='http://kingfisher.scene7.com/is/image/Kingfisher/3663602934806_03c')
    product22 = Product(name='Gas Pipe', brand='GasPipe', price=100, category='Gaspipe', image_url='https://images.search.yahoo.com/search/images;_ylt=AwriiI.byrhlnYkkJuaJzbkF;_ylu=c2VjA3NlYXJjaARzbGsDYnV0dG9u;_ylc=X1MDOTYwNjI4NTcEX3IDMgRmcgMEZnIyA3A6cyx2OmksbTpzYi10b3AEZ3ByaWQDX0tUTmtIUF9TS0dYLlRsTWFfNS5PQQRuX3JzbHQDMARuX3N1Z2cDMgRvcmlnaW4DaW1hZ2VzLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzEyBHF1ZXJ5A2xwZyUyMGdhcyUyMHBpcGUEdF9zdG1wAzE3MDY2MDk0MzY-?p=lpg+gas+pipe&fr=&fr2=p%3As%2Cv%3Ai%2Cm%3Asb-top&ei=UTF-8&x=wrt#id=0&iurl=https%3A%2F%2F5.imimg.com%2Fdata5%2FEV%2FVF%2FMY-55676695%2Flpg-gas-pipe-500x500.jpg&action=click')
    product23 = Product(name='kGas 6kg refill', brand='kGas', price=1800, category='Gas', image_url='https://kegasdealers.com/wp-content/uploads/2021/03/K-gas-6kg-gas-cylinder.jpg')
    product24 = Product(name='Total 6kg refill', brand='Total', price=2000, category='Gas', image_url='https://apps.gobeba.com/wp-content/uploads/2019/05/total-6kg-200x200.png')


    # # Create sample data for Customers
    # customer1 = Customer(first_name='John', last_name='Doe', gender='Male', phone_number='1234567890', email='john@example.com', password='customer1')
    # customer2 = Customer(first_name='Jane', last_name='Doe', gender='Female', phone_number='9876543210', email='jane@example.com', password='customer2')

    # Create sample data for Orders
    # order1 = Order(product_id=5, customer_id=2, time_ordered=datetime.utcnow())
    # order2 = Order(product_id=3, customer_id=1, time_ordered=datetime.utcnow())
    # order3 = Order(product_id=10, customer_id=3, time_ordered=datetime.utcnow())
    # order4 = Order(product_id=18, customer_id=3, time_ordered=datetime.utcnow())
    # order5 = Order(product_id=7, customer_id=1, time_ordered=datetime.utcnow())

    # Create sample data for Cart Items
    cart_item1 = Cart_Item(product_id=4, customer_id=2)
    cart_item2 = Cart_Item(product_id=12, customer_id=1)

    # Add sample data to the session
    db.session.add_all([ product3, product4, product5, product6, product7,
                        product8, product9, product10, product11, product12, product13, product14, product15,
                        product16, product17, product18, product19, product20, product21, product22, product23, product24])
    # db.session.add_all([order1, order2, order3, order4, order5])
    db.session.add_all([cart_item1, cart_item2])


    # Commit the session to persist the data
    db.session.commit()
