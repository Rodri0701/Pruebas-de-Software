from flask import Flask, Response
#from flask import Resource, reqparse, fields, marshal_with,abort
from flask_restful import reqparse, Api, Resource, reqparse, fields, marshal_with, abort
from api.models import User, Product, Order,OrderProduct,db
import json
import re


#Definicion de argumentos para agregar productos
product_args = reqparse.RequestParser()
product_args.add_argument("name", type=str, required = True, help="Name of the product is required")
product_args.add_argument("price", type=float,  required = True, help="Price of the product is required")
product_args.add_argument("quantity", type=int,  required = True, help="Quantity of the product is required")
product_args.add_argument("description", type=str,  required = True, help="Description of the product is required")
#CAMPOS DE SALIDA
productsFilds={
    'name': fields.String,
    'price': fields.Float,
    'quantity': fields.Integer,
    'description': fields.String
}

#definicion de argumentos para agregar usuarios
user_args = reqparse.RequestParser()
user_args.add_argument("username", type=str, required = True,help="Name of the user is required")
user_args.add_argument("password", type=str, required = True,help="Password of the user is required")
user_args.add_argument("email", type=str, required = True,help="Email of the user is required")
user_args.add_argument("phone", type=str, required = True,help="Phone of the user is required")
user_args.add_argument("address", type=str, required = True, help="Address of the user is required")
user_args.add_argument("is_admin", type=bool, required = True, help="Is admin of the user is required")
#CAMPOS DE SALIDA
userFilds = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'email': fields.String,
    'phone': fields.String,
    'address': fields.String,
    'is_admin': fields.Boolean
}
#Definicion de argumentos para agregar ordenes
order_args = reqparse.RequestParser()
order_args.add_argument("product_id", type=int, help="Id of the product is required")
order_args.add_argument("quantity", type=int, help="Quantity of the product is required")
order_args.add_argument("user_id", type=int, help="Id of the user is required")
#CAMPOS DE SALIDA
orderFilds = {
    'id': fields.Integer,
    'product_id': fields.Integer,
    'quantity': fields.Integer,
    'user_id': fields.Integer
}

#Metodos y validaciones para usuaruis
class User(Resource):
    @marshal_with(userFilds)
    #METODO GET PARA OBTENER
    def get(self): 
        user = User.query.all()
        if not user: 
            abort(404, message="User not found")
        return user,201
    
    #METODO PARA AGREGAR USUARIOS
    @marshal_with(userFilds)
    def post(self): #Agregar usuario
        args = user_args.parse_args()
        if not args['username'] or args['username'].isspace(): #PrimerValidación
            response = Response(json.dumps({'error': 'El nombre de usuario no puede ir vacio'}), 
            status=400, 
            mimetype='application/json')
            return abort(response)
        existe = User.query.filter_by(username=args['username']).first() #Segunda validación
        if existe:
            response = Response(json.dumps({'error': ' El nombre de usuario ya existe'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #Tercera validación (EMAIL)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", args['email']):
            response = Response(json.dumps({'error': 'El correo electrónico no es válido'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #CUARTA VALIDACIÓN (EMAIL VACIO)
        if not args['email'] or args['email'].isspace():
            response = Response(json.dumps({'error': 'El correo electrónico no puede ir vacio'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #QUINTA VALIDACIÓN (EMAIL EXISTENTE)
        existe = User.query.filter_by(email=args['email']).first()
        if existe:
            response = Response(json.dumps({'error': ' El correo electrónico ya existe'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #Sexta validación (PASSWORD VACIA)
        if not args['password'] or args['password'].isspace():
            response = Response(json.dumps({'error': 'La contraseña no puede ir vacia'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #SEPTIMA VALIDACIÓN (PASSWORD MENOR A 8 CARACTERES)
        if len(args['password']) < 8:
            response = Response(json.dumps({'error': 'La contraseña debe tener al menos 8 caracteres'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #OCTAVA VALIDACIÓN (PASSWORD MAYOR A 20 CARACTERES)
        if len(args['password']) > 50:
            response = Response(json.dumps({'error': 'La contraseña debe tener menos de 20 caracteres'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #NUEVA VALIDACIÓN (PASSWORD CON LETRAS MAYUSCULAS)
        if not re.search(r'[A-Z]', args['password']):
            response = Response(json.dumps({'error': 'La contraseña debe tener al menos una letra mayúscula'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #NUEVA VALIDACIÓN (PASSWORD CON LETRAS MINUSCULAS)
        if not re.search(r'[a-z]', args['password']):
            response = Response(json.dumps({'error': 'La contraseña debe tener al menos una letra minúscula'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #NUEVA VALIDACIÓN (PASSWORD CON NUMEROS)
        if not re.search(r'\d', args['password']):
            response = Response(json.dumps({'error': 'La contraseña debe tener al menos un número'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #DECIMA VALIDACION (PASSWORD CON CARACTERES ESPECIALES)
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', args['password']):
            response = Response(json.dumps({'error': 'La contraseña debe tener al menos un carácter especial'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #ONCEAVA VALIDACIÓN (PHONE VACIO)
        if not args['phone'] or args['phone'].isspace():
            response = Response(json.dumps({'error': 'El teléfono no puede ir vacio'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #DOCEAVA VALIDACIÓN (PHONE EXISTENTE)
        existe = User.query.filter_by(phone=args['phone']).first()
        if existe:
            response = Response(json.dumps({'error': ' El teléfono ya existe'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #TRECEAVA VALIDACION(ADDRESS VACIO)
        if not args['address'] or args['address'].isspace():
            response = Response(json.dumps({'error': 'La dirección no puede ir vacia'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #CATORCEAVA VALIDACION (ADDRESS EXISTENTE)
        existe = User.query.filter_by(address=args['address']).first()
        if existe:
            response = Response(json.dumps({'error': ' La dirección ya existe'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        
    #Actualizar usuarios
    @marshal_with(userFilds)
    def put(self, id):
        args = user_args.request.get_json()
        user= User.query.get(id)
        if not user:
            abort(404, message="Usuario no encontrado")
        user.username = args['username']
        user.email = args['email']
        user.password = args['password']
        user.phone = args['phone']
        user.address = args['address']
        db.session.commit()
        return user, 200
    
    #Borrar usuarios
    @marshal_with(userFilds)
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if not user:
            abort(404, message="Usuario no encontrado")
        db.session.delete(user)
        db.session.commit()
        users = User.query.all()
        return users, 200
    
#CLASE PARA AGREGAR Y VALIDAR PRODUCTOS
class Product(Resource):
    #VER TODOS LOS PRODUCTOS
    @marshal_with(productsFilds)
    def get(self):
        products = Product.query.all()
        if not products:
            abort(404, message="No hay productos")
        return products, 200
    
    #AGREGAR PRODUCTOS
    @marshal_with(productsFilds)
    def post(self):
        args = product_args.parse_args()
        #VALIDACION 1 (Producto vacio)
        if not args['name'] or args['name'].isspace():
            response = Response(json.dumps({'error': 'El nombre del producto no puede ir vacio'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #VALIDACION 2 (El prodcuto ya existe)
        existe = Product.query.filter_by(name=args['name']).first()
        if existe:
            response = Response(json.dumps({'error': ' El nombre del producto ya existe'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #VALIDACION 3 (El producto no puede tener un precio menor a 0)
        if args['price'] < 0:
                response = Response(json.dumps({'error': 'El precio del producto no puede ser negativo'}),
                status=400,
                mimetype='application/json')
                return abort(response)
        #VALIDACION 4 (El producto no puede ser superior a un millon)
        if args['price'] > 1000000:
                    response = Response(json.dumps({'error': 'El precio del producto no puede ser mayor a 1,000,000'}),
                    status=400,
                    mimetype='application/json')
                    return abort(response)
        #VALIDACION 5 (El precio solo son numeros enteros)
        if not args['price'].replace('.', '', 1).isdigit():
            response = Response(json.dumps({'error': 'El precio del producto solo puede ser un numero enteros'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #VALIDACION 6 (La cantidad del producto no puede ser negativa)
        if args['quantity'] < 0:
            response = Response(json.dumps({'error': 'La cantidad del producto no puede ser negativa'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #VALIDACION 7 (La cantidad del producto no puede ser mayor a 1000)
        if args['quantity'] > 1000:
            response = Response(json.dumps({'error': 'La cantidad del producto no puede ser mayor a 1,000'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #VALIDACION 8 (La cantidad del producto no puede ser un decimal)
        if not args['quantity'].replace('.', '', 1).isdigit():
            response = Response(json.dumps({'error': 'La cantidad del producto no puede ser un decimal'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #VALIDACION 9 (La cantidad del producto no puede ir vacia)
        if not args['quantity'] or args['quantity'].isspace():
            response = Response(json.dumps({'error': 'La cantidad del producto no puede ir vacia'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        #VALIDACION 10 (La descripcion del producto no puede ir vacia)
        if not args['description'] or args['description'].isspace():
            response = Response(json.dumps({'error': 'La descripción del producto no puede ir vacia'}),
            status=400,
            mimetype='application/json')
            return abort(response)
        product = Product(name=args['name'], price=args['price'], quantity=args['quantity'], description=args['description'])
        db.session.add(product)
        db.session.commit()
        return product, 201
    
    #ACTUALIZAR PRODUCTOS
    @marshal_with(productsFilds)
    def put(self, id):
        args = product_args.parse_args()
        product = Product.query.get(id)
        if product is None:
            response = Response(json.dumps({'error': 'El producto no existe'}),
                                status=404,
                                mimetype='application/json')
            return abort(response)
        product.name = args['name']
        product.price = args['price']
        product.quantity = args['quantity']
        product.description = args['description']
        db.session.commit()
        return product, 200
    
    #BORRAR PRODUCTOS
    @marshal_with(productsFilds)
    def delete(self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            abort(404, message="Producto no encontrado")
        db.session.delete(product)
        db.session.commit()
        products=Product.query.all()
        return products, 200
    
#CLASE PARA DEFINIR ORDENES
class Order(Resource):
    #VER ORDENES
    @marshal_with(orderFilds)
    def get(self, id):
        orders= Order.query.filter_by(id=id).first()
        if not orders:
            abort(404, message="No hay ordenes")
        return orders, 200
    
    #CREAR ORDENES
    @marshal_with(orderFilds)
    def post(self):
        args = order_args.parse_args()
        order = Order(name=args['name'], price=args['price'], quantity=args['quantity'], description=args['description'])
        db.session.add(order)
        db.session.commit()
        return order, 201
        
    #ACTUALIZAR ORDENES
    @marshal_with(orderFilds)
    def put(self, id):
        args = order_args.parse_args()
        order = Order.query.get(id)
        if order is None:
            response = Response(json.dumps({'error': 'La orden no existe'}),
                                status=404,
                                mimetype='application/json')
            return abort(response)
        order.name = args['name']
        order.price = args['price']
        order.quantity = args['quantity']
        order.description = args['description']
        db.session.commit()
        return order, 200
    
    #BORAR ORDENES
    @marshal_with(orderFilds)
    def delete(self, id):
        order = Order.query.filter_by(id=id).first()
        if not order:
            abort(404, message="Orden no encontrada")
        db.session.delete(order)
        db.session.commit()
        orders=Order.query.all()
        return orders, 200
    
    #EDITAR ORDENES
    def patch(self, id):
        args = order_args.parse_args()
        order = Order.query.get(id)
        if order is None:
            response = Response(json.dumps({'error': 'La orden no existe'}),
                                status=404,
                                mimetype='application/json')
            return abort(response)
        order.name = args['name']
        order.price = args['price']
        order.quantity = args['quantity']
        order.description = args['description']
        db.session.commit()
        return order, 200
