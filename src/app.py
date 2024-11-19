from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_restful import reqparse
from api.extension import db
from api.controllers import User, Product, Order, OrderProduct, Department

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Almacen_SF.db'
db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()

api.add_resource(User, '/user/<int:idUser>')
api.add_resource(Product, '/product/<int:product_id>')
api.add_resource(Order, '/order/<int:order_id>')
api.add_resource(Department, '/Department/<int:Deparmant_id>')

@app.route('/')
def index():
    return '<h1> Almacen SF </h1>'

if __name__ == '__main__':
    app.run(debug=True)