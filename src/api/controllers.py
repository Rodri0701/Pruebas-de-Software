from flask import Flask, Response
#from flask import Resource, reqparse, fields, marshal_with,abort
from flask_restful import reqparse, Api, Resource, reqparse, fields, marshal_with, abort
from api.models import UserModel, ProductModel, OrderModel, OrderProductModel, db
import json
import re
from flask_restful import reqparse


#----------------------------------------------USUARIOS----------------------------------------------#
user_args = reqparse.RequestParser()
user_args.add_argument("username", type=str, required=True, help="Name of the user is required")
user_args.add_argument("password", type=str, required=True, help="Password of the user is required")
user_args.add_argument("email", type=str, required=True, help="Email of the user is required")
user_args.add_argument("phone", type=str, required=True, help="Phone of the user is required")
user_args.add_argument("address", type=str, required=True, help="Address of the user is required")

 #CAPOS DE SALIDA
userFields = {
    'idUser': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'email': fields.String,
    'address': fields.String,
    'phone': fields.String
    
    
}
#CLASE PARA VER O AGREGAR DE TODOS LOS USUARIOS
class Users(Resource):
    #OBTENER TODOS LOS USUARIOS
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users
    #AGREGAR UN USUARIO
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
       #1era VALIDACION (nombre de usuario vacio)
        if not args['username'] or args['username'].isspace():
            response = Response(json.dumps({'error': 'Username cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)
        #2da VALIDACION (nombre de usuario con espacios)
        if re.search(r'\s', args['username']):
            response = Response(json.dumps({'error': 'Username cannot contain spaces'}), status=400, mimetype='application/json')
            return abort(response)
        #3ra VALIDACION (nombre de usuario con caracteres especiales)
        if not re.match(r'^[a-zA-Z0-9]+$', args['username']):
            response = Response(json.dumps({'error': 'Username cannot contain special characters'}), status=400, mimetype='application/json')
            return abort(response)
        #4ta VALIDACION (nombre de usuario con menos de 3 caracteres)
        if len(args['username']) < 3:
            response = Response(json.dumps({'error': 'Username must be at least 3 characters long'}), status=400, mimetype='application/json')
            return abort(response)
        #5ta VALIDACION (nombre de usuario con mas de 20 caracteres)
        if len(args['username']) > 20:
            response = Response(json.dumps({'error': 'Username cannot be longer than 20 characters'}), status=400, mimetype='application/json')
            return abort(response)
        #6ta VALIDACION (nombre de usuario repetido)
        if UserModel.query.filter_by(username=args['username']).first():
            response = Response(json.dumps({'error': 'Username already exists'}), status=400, mimetype='application/json')
            return abort(response)
        #7ma VALIDACION (contraseña vacia)
        if not args['password'] or args['password'].isspace():
            response = Response(json.dumps({'error': 'Password cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)
        #8va VALIDACION (contraseña con espacios)
        if re.search(r'\s', args['password']):
            response = Response(json.dumps({'error': 'Password cannot contain spaces'}), status=400, mimetype='application/json')
            return abort(response)
        #9na VALIDACION (contraseña con menos de 8 caracteres)
        if len(args['password']) < 8:
            response = Response(json.dumps({'error': 'Password must be at least 8 characters long'}), status=400, mimetype='application/json')
            return abort(response)
        #10ma VALIDACION (contraseña con mas de 20 caracteres)
        if len(args['password']) > 20:
            response = Response(json.dumps({'error': 'Password cannot be longer than 20 characters'}), status=400, mimetype='application/json')
            return abort(response)
        #11va VALIDACION (email vacio)
        if not args['email'] or args['email'].isspace():
            response = Response(json.dumps({'error': 'Email cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)
        #12va VALIDACION (email con espacios)
        if re.search(r'\s', args['email']):
            response = Response(json.dumps({'error': 'Email cannot contain spaces'}), status=400, mimetype='application/json')
            return abort(response)
        #13va VALIDACION (que el email tenga un @)
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', args['email']):
            response = Response(json.dumps({'error': 'Invalid email format'}), status=400, mimetype='application/json')
            return abort(response)
        #14va VALIDACION (email repetido)
        if UserModel.query.filter_by(email=args['email']).first():
            response = Response(json.dumps({'error': 'Email already exists'}), status=400, mimetype='application/json')
            return abort(response)
        #15va VALIDACION (telefono vacio)
        if not args['phone'] or args['phone'].isspace():
            response = Response(json.dumps({'error': 'Phone cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)
        #16va VALIDACION (telefono con espacios)
        if re.search(r'\s', args['phone']):
            response = Response(json.dumps({'error': 'Phone cannot contain spaces'}), status=400, mimetype='application/json')
            return abort(response)
        #17va VALIDACION (que el telefono tenga 10 digitos)
        if len(args['phone']) != 10:
            response = Response(json.dumps({'error': 'Invalid phone number'}), status=400, mimetype='application/json')
            return abort(response)
        #18va VALIDACION (que el telefono no tenga letras)
        if not re.match(r'^[0-9]+$', args['phone']):
            response = Response(json.dumps({'error': 'Invalid phone number'}), status=400, mimetype='application/json')
            return abort(response)
        #19va VALIDACION (telefono repetido)
        if UserModel.query.filter_by(phone=args['phone']).first():
            response = Response(json.dumps({'error': 'Phone already exists'}), status=400, mimetype='application/json')
            return abort(response)
        #20va VALIDACION (dirección vacio)
        if not args['address'] or args['address'].isspace():
            response = Response(json.dumps({'error': 'Address cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)
        #21va VALIDACION (La direccion debe llevar un #)
        if not re.search(r'#', args['address']):
            response = Response(json.dumps({'error': 'Address must contain a #'}), status=400, mimetype='application/json')
            return abort(response)
        
        user = UserModel(username=args['username'], password=args['password'], email=args['email'], phone=args['phone'], address=args['address'])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201
    
#CLASE PARA VER, ELIMINAR O EDITAR UN SOLO USUARIO    
class User(Resource):
    #OBTENER UN USUARIO
    @marshal_with(userFields)
    def get(self, idUser):
        user = UserModel.query.filter_by(idUser=idUser).first()
        if not user:
            response = Response(json.dumps({'error': 'User not found'}), status=404, mimetype='application/json')
            return abort(response)
        return user, 200
    #ELIMINAR UN USUARIO
    def delete(self, idUser):
        user = UserModel.query.filter_by(idUser=idUser).first()
        if not user:
            response = Response(json.dumps({'error': 'User not found'}), status=404, mimetype='application/json')
            return abort(response)
        db.session.delete(user)
        db.session.commit()
        return 'User deleted', 204
    #EDITAR UN USUARIO
    @marshal_with(userFields)
    def put(self, idUser):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(idUser=idUser).first()
        
        if not user:
            response = Response(json.dumps({'error': 'User not found'}), status=404, mimetype='application/json')
            return abort(response)
        
        # Validaciones (si el campo fue modificado y debe validarse)
        if not args['username'] or args['username'].isspace():
            response = Response(json.dumps({'error': 'Username cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)

        if re.search(r'\s', args['username']):
            response = Response(json.dumps({'error': 'Username cannot contain spaces'}), status=400, mimetype='application/json')
            return abort(response)

        if not re.match(r'^[a-zA-Z0-9]+$', args['username']):
            response = Response(json.dumps({'error': 'Username cannot contain special characters'}), status=400, mimetype='application/json')
            return abort(response)

        if len(args['username']) < 3:
            response = Response(json.dumps({'error': 'Username must be at least 3 characters long'}), status=400, mimetype='application/json')
            return abort(response)

        if len(args['username']) > 20:
            response = Response(json.dumps({'error': 'Username cannot be longer than 20 characters'}), status=400, mimetype='application/json')
            return abort(response)

        if UserModel.query.filter_by(username=args['username']).first() and args['username'] != user.username:
            response = Response(json.dumps({'error': 'Username already exists'}), status=400, mimetype='application/json')
            return abort(response)

        if not args['password'] or args['password'].isspace():
            response = Response(json.dumps({'error': 'Password cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)

        if re.search(r'\s', args['password']):
            response = Response(json.dumps({'error': 'Password cannot contain spaces'}), status=400, mimetype='application/json')
            return abort(response)

        if len(args['password']) < 8:
            response = Response(json.dumps({'error': 'Password must be at least 8 characters long'}), status=400, mimetype='application/json')
            return abort(response)

        if len(args['password']) > 20:
            response = Response(json.dumps({'error': 'Password cannot be longer than 20 characters'}), status=400, mimetype='application/json')
            return abort(response)

        if not args['email'] or args['email'].isspace():
            response = Response(json.dumps({'error': 'Email cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)

        if re.search(r'\s', args['email']):
            response = Response(json.dumps({'error': 'Email cannot contain spaces'}), status=400, mimetype='application/json')
            return abort(response)

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', args['email']):
            response = Response(json.dumps({'error': 'Invalid email format'}), status=400, mimetype='application/json')
            return abort(response)

        if UserModel.query.filter_by(email=args['email']).first() and args['email'] != user.email:
            response = Response(json.dumps({'error': 'Email already exists'}), status=400, mimetype='application/json')
            return abort(response)

        if not args['phone'] or args['phone'].isspace():
            response = Response(json.dumps({'error': 'Phone cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)

        if re.search(r'\s', args['phone']):
            response = Response(json.dumps({'error': 'Phone cannot contain spaces'}), status=400, mimetype='application/json')
            return abort(response)

        if len(args['phone']) != 10:
            response = Response(json.dumps({'error': 'Invalid phone number'}), status=400, mimetype='application/json')
            return abort(response)

        if not re.match(r'^[0-9]+$', args['phone']):
            response = Response(json.dumps({'error': 'Invalid phone number'}), status=400, mimetype='application/json')
            return abort(response)

        if UserModel.query.filter_by(phone=args['phone']).first() and args['phone'] != user.phone:
            response = Response(json.dumps({'error': 'Phone already exists'}), status=400, mimetype='application/json')
            return abort(response)

        user = UserModel.query.filter_by(idUser=idUser).first()

        if not user:
            response = Response(json.dumps({'error': 'User not found'}), status=404, mimetype='application/json')
            return response
        user.username = args['username']
        user.password = args['password']
        user.email = args['email']
        user.address = args['address']
        user.phone = args['phone']

        try:
            db.session.commit()
            return user, 200
        except Exception as e:
            db.session.rollback()  # Revertir cambios si hay un error
            return user, 401

       
#----------------------------------------------USUARIOS----------------------------------------------#

product_args = reqparse.RequestParser()
product_args.add_argument('name', type=str, required=True, help='Name cannot be blank')
product_args.add_argument('price', type=float, required=True, help='Price cannot be blank')
product_args.add_argument('quantity', type=int, required=True, help='Quantity cannot be blank')
product_args.add_argument('description', type=str, required=True, help='Description cannot be blank')
product_args.add_argument('stock', type=int, required=True, help='Stock cannot be blank')

#CAMPOS DE SALIDA
productFields = {
    'idProduct': fields.Integer,
    'name': fields.String,
    'price': fields.Float,
    'quantity': fields.Integer,
    'description': fields.String,
    'stock': fields.Integer
}

#CLASE PARA VER O AGREGAR TODOS LOS PRODUCTOS
class Products(Resource):
    #OBTENER TODOS LOS PRODUCTOS
    @marshal_with(productFields)
    def get(self):
        products = ProductModel.query.all()
        return products, 200
    #AGREGAR UN PRODUCTO
    @marshal_with(productFields)
    def post(self):
        args = product_args.parse_args()
        #1era VALIDACION (nombre vacio)
        if not args['name'] or args['name'].isspace():
            response = Response(json.dumps({'error': 'Name cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)
        #2da VALIDACION (nombre con caracteres especiales)
        if re.search(r'[^a-zA-Z0-9\s]', args['name']):
            response = Response(json.dumps({'error': 'Name cannot contain special characters'}), status=400, mimetype='application/json')
            return abort(response)
        #3era VALIDACION (nombre repetido)
        if ProductModel.query.filter_by(name=args['name']).first():
            response = Response(json.dumps({'error': 'Name already exists'}), status=400, mimetype='application/json')
            return abort(response)
        #4ta VALIDACION (precio vacio)
        if not args['price']:
            response = Response(json.dumps({'error': 'Price cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)
        #5ta VALIDACION (precio negativo)
        if args['price'] < 0:
            response = Response(json.dumps({'error': 'Price cannot be negative'}), status=400, mimetype='application/json')
            return abort(response)
        #6ta VALIDACION (no poner letras en el precio)
        if not re.match(r'^\d+(\.\d+)?$', str(args['price']).strip()):
            response = Response(json.dumps({'error': 'Price must be a valid number without letters'}), status=400, mimetype='application/json')
            return abort(response)
        #7ma VALIDACION (precio minimo 100.00)
        if args['price'] < 100.00:
            response = Response(json.dumps({'error': 'Price must be at least 100.00'}), status=400, mimetype='application/json')
            return abort(response)
        #8va VALIDACION (precio maximo 100000.00)
        if args['price'] > 100000.00:
            response = Response(json.dumps({'error': 'Price cannot be more than 10000.00'}), status=400, mimetype='application/json')
            return abort(response)
        #9na VALIDACION (descripcion vacia)
        if not args['description'] or args['description'].isspace():
            response = Response(json.dumps({'error': 'Description cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)
        #10ma VALIDACION (descripcion minima 10 carateres)
        if len(args['description']) < 10:
            response = Response(json.dumps({'error': 'Description must be at least 10 characters long'}), status=400, mimetype='application/json')
            return abort(response)
        #11ma VALIDACION (descripcion maxima 1000 carateres)
        if len(args['description']) > 1000:
            response = Response(json.dumps({'error': 'Description cannot be longer than 1000 characters'}), status=400, mimetype='application/json')
            return abort(response)
        #12va VALIDACION (stock vacio)
        if not args['stock']:
            response = Response(json.dumps({'error': 'Stock cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)
        #13va VALIDACION (stock negativo)
        if args['stock'] < 0:
            response = Response(json.dumps({'error': 'Stock cannot be negative'}), status=400, mimetype='application/json')
            return abort(response)
        #14ma VALIDACION (no poner letras en el stock)
        if not re.match(r'^[0-9]+$', str(args['stock'])):
            response = Response(json.dumps({'error': 'Stock cannot contain letters'}), status=400, mimetype='application/json')
            return abort(response)
        #15ma VALIDACION (stock minimo 1)
        if args['stock'] < 1:
            response = Response(json.dumps({'error': 'Stock must be at least 1'}), status=400, mimetype='application/json')
            return abort(response)
        #16ma VALIDACION (stock maximo 1000)
        if args['stock'] > 1000:
            response = Response(json.dumps({'error': 'Stock cannot be more than 1000'}), status=400, mimetype='application/json')
            return abort(response)
        
        product = ProductModel(name=args['name'], price=args['price'], quantity= args['quantity'] ,description=args['description'], stock=args['stock'])
        db.session.add(product)
        db.session.commit()
        products = ProductModel.query.all()
        return products, 201

#CLASE PARA VER, EDITAR O ELIMINAR UN PRODUCTO
class Product(Resource):
    #OBTENER UN SOLO PRODUCTOS
    @marshal_with(productFields)
    def get(self, idProduct):
        product = ProductModel.query.get(idProduct)
        if not product:
           if not product:
            response = Response(json.dumps({'error': 'Product not found'}), status=404, mimetype='application/json')
            return abort(response)
        return product, 200
    #ELIMINAR UN PRODUCTO
    @marshal_with(productFields)
    def delete(self, idProduct):
        product = ProductModel.query.get(idProduct)
        if not product:
            response = Response(json.dumps({'error': 'Product not found'}), status=404, mimetype='application/json')
            return abort(response)
        db.session.delete(product)
        db.session.commit()
        products = ProductModel.query.all()
        return products, 200
    #EDITAR UN PRODUCTO
    @marshal_with(productFields)
    def put(self, idProduct):
        args = product_args.parse_args()
        product = ProductModel.query.get(idProduct)
        #1era VALIDACION (nombre vacio)
        if not args['name'] or args['name'].isspace():
            response = Response(json.dumps({'error': 'Name cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)
        #2da VALIDACION (nombre con caracteres especiales)
        if re.search(r'[^a-zA-Z0-9\s]', args['name']):
            response = Response(json.dumps({'error': 'Name cannot contain special characters'}), status=400, mimetype='application/json')
            return abort(response)
        #3era VALIDACION (nombre repetido)
        #if ProductModel.query.filter_by(name=args['name']).first():
         #   response = Response(json.dumps({'error': 'Name already exists'}), status=400, mimetype='application/json')
          #  return abort(response)
        #4ta VALIDACION (precio vacio)
        if not args['price']:
            response = Response(json.dumps({'error': 'Price cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)
        #5ta VALIDACION (precio negativo)
        if args['price'] < 0:
            response = Response(json.dumps({'error': 'Price cannot be negative'}), status=400, mimetype='application/json')
            return abort(response)
        #6ta VALIDACION (no poner letras en el precio)
        if not re.match(r'^\d+(\.\d+)?$', str(args['price']).strip()):
            response = Response(json.dumps({'error': 'Price must be a valid number without letters'}), status=400, mimetype='application/json')
            return abort(response)
        #7ma VALIDACION (precio minimo 100.00)
        if args['price'] < 100.00:
            response = Response(json.dumps({'error': 'Price must be at least 100.00'}), status=400, mimetype='application/json')
            return abort(response)
        #8va VALIDACION (precio maximo 100000.00)
        if args['price'] > 100000.00:
            response = Response(json.dumps({'error': 'Price cannot be more than 10000.00'}), status=400, mimetype='application/json')
            return abort(response)
        #9na VALIDACION (descripcion vacia)
        if not args['description'] or args['description'].isspace():
            response = Response(json.dumps({'error': 'Description cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)
        #10ma VALIDACION (descripcion minima 10 carateres)
        if len(args['description']) < 10:
            response = Response(json.dumps({'error': 'Description must be at least 10 characters long'}), status=400, mimetype='application/json')
            return abort(response)
        #11ma VALIDACION (descripcion maxima 1000 carateres)
        if len(args['description']) > 1000:
            response = Response(json.dumps({'error': 'Description cannot be longer than 1000 characters'}), status=400, mimetype='application/json')
            return abort(response)
        #12va VALIDACION (stock vacio)
        if not args['stock']:
            response = Response(json.dumps({'error': 'Stock cannot be empty'}), status=400, mimetype='application/json')
            return abort(response)
        #13va VALIDACION (stock negativo)
        if args['stock'] < 0:
            response = Response(json.dumps({'error': 'Stock cannot be negative'}), status=400, mimetype='application/json')
            return abort(response)
        #14ma VALIDACION (no poner letras en el stock)
        if not re.match(r'^[0-9]+$', str(args['stock'])):
            response = Response(json.dumps({'error': 'Stock cannot contain letters'}), status=400, mimetype='application/json')
            return abort(response)
        #15ma VALIDACION (stock minimo 1)
        if args['stock'] < 1:
            response = Response(json.dumps({'error': 'Stock must be at least 1'}), status=400, mimetype='application/json')
            return abort(response)
        #16ma VALIDACION (stock maximo 1000)
        if args['stock'] > 1000:
            response = Response(json.dumps({'error': 'Stock cannot be more than 1000'}), status=400, mimetype='application/json')
            return abort(response)
        
        product = ProductModel.query.filter_by(idProduct=idProduct).first()
        if not product:
            response = Response(json.dumps({'error': 'Product not found'}), status=404, mimetype='application/json')
            return abort(response)
        
        product.name = args['name']
        product.price = args['price']
        product.quantity = args['quantity']
        product.description = args['description']
        product.stock = args['stock']

        try:
            db.session.commit()
            return product, 200
        except Exception as e:
            db.session.rollback()
            return product, 500
#----------------------------------------------PRODUCTOS----------------------------------------------#


#----------------------------------------------PRODUCTOS----------------------------------------------#


#----------------------------------------------DEPARTAMENTO----------------------------------------------#


#----------------------------------------------DEPARTAMENTO----------------------------------------------#


#----------------------------------------------ORDENES----------------------------------------------#


#----------------------------------------------ORDENES----------------------------------------------#

#----------------------------------------------ORDENES-PRODUCTOS----------------------------------------------#

#----------------------------------------------ORDENES-PRODUCTOS----------------------------------------------#