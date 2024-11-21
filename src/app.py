from flask import Flask
from flask_restful import Api
from api.extension import db
from api.controllers import Users, User, Product,Products,Departments, Department, Orders, Order, OrdersProducts, OrderProduct


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

api.add_resource(Departments, '/api/Department/') #Ruta para ver TODOS LOS DEPARTAMENTOS
api.add_resource(Department, '/api/Department/<int:idDepartment>') #Ruta para ver UN DEPARTAMENTO

api.add_resource(Orders, '/api/Order/') #Ruta para ver TODAS LAS ORDENES
api.add_resource(Order, '/api/Order/<int:idOrder>') #Ruta para ver UNA ORDEN

api.add_resource(OrdersProducts, '/api/OrderProduct/') #Ruta para ver TODOS LOS PRODUCTOS DE UNA ORDEN
api.add_resource(OrderProduct, '/api/OrderProduct/<int:idOrderProduct>') #Ruta para ver UN PRODUCTO DE UNA ORDEN


@app.route('/')
def index():
    return '<h1> Almacen SF </h1>'

if __name__ == '__main__':
    app.run(debug=True)