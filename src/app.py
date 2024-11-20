from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_restful import reqparse
from api.extension import db
from api.controllers import Users, User, Product,Products


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Almacen_SF.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

#ruta para la vista (usuarios)

api.add_resource(Users, '/api/User/') #Ruta para ver TODOS LOS USUARIOS
api.add_resource(User, '/api/User/<int:idUser>') #Ruta para ver UN USUARIO

api.add_resource(Products, '/api/Product/') #Ruta para ver TODOS LOS PRODUCTOS
api.add_resource(Product, '/api/Product/<int:idProduct>') #Ruta para ver UN PRODUCTO 


@app.route('/')
def index():
    return '<h1> Almacen SF </h1>'

if __name__ == '__main__':
    app.run(debug=True)