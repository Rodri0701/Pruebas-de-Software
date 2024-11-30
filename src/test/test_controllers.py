from flask.testing import FlaskClient
import pytest
import unittest
from flask import Flask,json
from api.models import db, UserModel,ProductModel,OrderModel,OrderProductModel,DepartmentModel
from api.controllers import User, Users, Product, Products, Order, Orders, Department, Departments, OrderProduct, OrdersProducts
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource,reqparse
from unittest.mock import patch, MagicMock, Mock
from flask import Flask, Response
#from flask import Resource, reqparse, fields, marshal_with,abort
from flask_restful import reqparse, Api, Resource, reqparse, fields, marshal_with, abort
from api.models import UserModel, ProductModel, OrderModel, OrderProductModel,DepartmentModel ,db
import json
import re
from flask_restful import reqparse
from flask_restful import reqparse
from datetime import datetime



@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Base de datos en memoria para pruebas
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api = Api(app)
    
    # Registrar rutas
    api.add_resource(Users, '/api/User/')
    api.add_resource(User, '/api/User/<int:idUser>')
    api.add_resource(Products, '/api/Product/')
    api.add_resource(Product, '/api/Product/<int:idProduct>')
    api.add_resource(Departments, '/api/Department/')
    api.add_resource(Department, '/api/Department/<int:idDepartment>')
    api.add_resource(Orders, '/api/Order/')
    api.add_resource(Order, '/api/Order/<int:idOrder>')
    api.add_resource(OrdersProducts, '/api/OrderProduct/')
    api.add_resource(OrderProduct, '/api/OrderProduct/<int:idOrderProduct>')

    with app.app_context():
        db.create_all()  # Crear las tablas en la base de datos

    yield app

    with app.app_context():
        db.drop_all()  # Eliminar las tablas después de las pruebas

#-----------------------------------PYTEST-----------------------------------#

@pytest.fixture
def client(app: Flask):
    return app.test_client()
#PRUEBA 1
#OBTENER USUARIOS
def test_get_users(client):
    response = client.get('/api/User/')
    assert response.status_code == 200
    assert response.json == []



#PRUEBA 2
#INSERTAR UN USUARIO.
def test_insert_user(client):
 response = client.post('/api/User/', json={
        "username": "JoSeLo",
        "password": "ContraSegura2",
        "email": "redCuervo@gmail.com",
        "phone": 4499506008,
        "address": "La calle #245",
        "role": "Employee"
     })
 assert response.status_code == 201
 data = json.loads(response.data)
 assert len(data) == 1
 assert data[0]['username'] == 'JoSeLo'
 assert data[0]['password'] == 'ContraSegura2'
 assert data[0]['email'] == 'redCuervo@gmail.com'
 assert data[0]['phone'] == '4499506008'
 assert data[0]['address'] == 'La calle #245'
 assert data[0]['role'] == 'Employee'

#PRUEBA 3
 #INSERTAR CAMPOS VACIAS (PRUEBA DESTINADA A FALLAR (REVISAR EL JSON GENERADO CON EL ERROR))
def test_insert_user_empty_fields(client):
  user_data = {
    "username": " ",
        "password": "contrasegura",
        "email": "sadfjkn@gmail.com",
        "phone": 1234567981,
        "address": "sfhdsf #44",
        "role": "Employee"
  }
  client.post('/api/User/', json=user_data)
  response = client.post('/api/User/', json=user_data)
  assert response.status_code == 400
  assert response.json == {'error': 'Username cannot be empty'}
    
#PRUEBA 4
#INSERTAR UN USUARIO CON UN USERNAME YA EXISTENTE
def test_insert_user_existing_username(client):
        # Inserta un usuario con nombre de usuario duplicado
        user_data = {
            "username": "RoEsPa",
            "password": "ContraSegura",
            "email": "rodrigoesparza117@gmail.com",
            "phone": "4499506008",
            "address": "BasureroMuncipal #48451",
            "role": "admin"
        }
        client.post('/api/User/', json=user_data)  # Inserta el usuario duplicado
        response = client.post('/api/User/', json=user_data)

        # Verifica que la respuesta es la esperada: error 400
        assert response.status_code == 400
        assert response.json == {'error': 'Username already exists'}

     
#PRUEBA 5
#INSERTAR UN USUARIO CON UN EMAIL INVALIDO
def test_insert_user_existing_email(client):
        # Inserta un usuario con nombre de usuario duplicado
        user_data = {
            "username": "XXXXXX",
            "password": "XXXXXXXXXXXX",
            "email": "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "phone": "4499506008",
            "address": "BasureroMuncipal #48451",
            "role": "admin"
        }
        client.post('/api/User/', json=user_data)  # Inserta el usuario duplicado
        response = client.post('/api/User/', json=user_data)

        # Verifica que la respuesta es la esperada: error 400
        assert response.status_code == 400
        assert response.json == {'error': 'Invalid email format'}

#PRUEBA 6
#INSERTAR PHONE CON LETRAS
def test_insert_user_phone_letters(client):
        # Inserta un usuario con nombre de usuario duplicado
        user_data = {
            "username": "RoEsPa",
            "password": "XXXXXXXXXXXX",
            "email": "rodrigoesparza117@gmail.com",
            "phone": "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "address": "BasureroMuncipal #48451",
            "role": "admin"
        }
        client.post('/api/User/', json=user_data)  # Inserta el usuario duplicado
        response = client.post('/api/User/', json=user_data)

        # Verifica que la respuesta es la esperada: error 400
        assert response.status_code == 400
        assert response.json == {'error': 'Invalid phone number'}

#PRUEBA 7
#VERIFICAR EMAIL
def test_verify_email(client):
    mock_user_repository = MagicMock()
    mock_user_repository.get_all.return_value = {
     "email": "john@usebouncer.com",
        "status": "deliverable",
        "reason": "accepted_email",
        "domain": {
            "name": "usebouncer.com",
            "acceptAll": "no",
            "disposable": "no",
            "free": "no"
        },
        "account": {
            "role": "no",
            "disabled": "no",
            "fullMailbox": "no"
        },
        "dns": {
            "type": "MX",
            "record": "aspmx.l.google.com."
        },
        "provider": "google.com",
        "score": 100,
        "toxic": "unknown",
        "toxicity": 0
   }

    assert mock_user_repository.get_all.return_value['status'] == 'deliverable'
    assert mock_user_repository.get_all.return_value['reason'] == 'accepted_email'
#-----------------------------------PYTEST-----------------------------------#

#-----------------------------------PATCH-----------------------------------#
#PRUEBA 8
#OBTENER PRODUCTOS CON PATCH
@patch.object(Product, 'get')
def test_product_get(mock_get):
    mock_product = Mock()
    mock_product.idProduct = 1
    mock_product.name = 'Product1'
    mock_product.price = 10.99
    mock_product.description = "XXXXXXXXXXXXXXXXXX"
    mock_product.stock = 10
    mock_get.return_value = mock_product
    
    result = Product.get()
    assert result == mock_product
    assert result.idProduct == 1
    assert result.name == 'Product1'
    assert result.price == 10.99
    assert result.description == "XXXXXXXXXXXXXXXXXX"
    assert result.stock == 10


#CLASE PARA HACER TEST DE PRODUCTOS UNO A UNO
class TestProduct(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['DEBUG'] = True
        self.api = Api(self.app)
        self.api.add_resource(Product, '/api/Product/<int:idProduct>')
        self.client = self.app.test_client()

        self.app_context = self.app.app_context()
        self.app_context.push()

        db.init_app(self.app)
        db.create_all()
#PRUEBA 9 
#OBTENER UN PRODUCTO USANDO PATCH Y SU ID
    @patch('api.controllers.ProductModel.query')
    def test_get_product(self, mock_query):
        # Mock de la base de datos
        mock_query.get.return_value = ProductModel(
            idProduct=1, name='Papel impresora', price=205.45, 
            description="Papel que va dentro de la impresora", stock=50
        )
        
        # Hacer la solicitud GET con el ID adecuado
        response = self.client.get('/api/Product/1')  # Usa un valor real para el ID

        # Verificar la respuesta
        self.assertEqual(response.status_code, 200)
        self.assertIn('Papel impresora', response.get_data(as_text=True))
        self.assertIn('205.45', response.get_data(as_text=True))  # Verifica el contenido


#-----------------------------Productos-----------------------------------#
def log_response(response, message=""):
    print(f"\n{message}")
    print("Status Code:", response.status_code)
    print("Response Data:", response.data)
    return response
    
product_test_data = [
    {
        "name": "CocaCola Espumaa",
        "description": "Es una coquita bien fria",
        "price": 100.00,
        "stock": 50
    },
    {
        "name": "Pepsi",
        "description": "Es una pecsi bien fria",
        "price": 101.00,
        "stock": 51
    },
    {
        "name": "Fanta",
        "description": "Es una fantastic bien fria",
        "price": 103.00,
        "stock": 53
    }
]

#PRUEBA 1
#OBTENER PRODUCTOS
def test_get_products_empty(client):
    response = log_response(client.get('/api/Product/'), "Retrieving data")
    assert response.status_code == 200
    assert response.json == []

#PRUEBA 2
#INSERTAR UN PRODUCTO.
def test_insert_product(client):
    response = log_response(client.post('/api/Product/', json=product_test_data[0]), "Inserting data")
    assert response.status_code == 201
    assert len(response.json) == 1    
    
#PRUEBA 3
#INSERTAR(post) VALORES NULOS/VACIOS O INVALIDOS
@pytest.mark.parametrize("name,desc,price,stock",[
    (" ","Coquita sabrosa","100","100"),
    ("CocaCola", " ", "100", "100"),
    ("CocaCola", "Coquita sabrosa", None, "100"),
    ("CocaCola", "Coquita sabrosa", "100", None),
    ("Coc@Cola","Coquita sabrosa", "100", "100"),
    ("CocaCola", "Coquita sabrosa", "-10", "100"),
    ("CocaCola", "Coquita sabrosa", "100", "-10")
])
def test_insert_invalid_product_data(client,name,desc,price,stock):
    expected_errors = [
    "Name cannot be empty",
    "Description cannot be empty",
    "Price cannot be empty",
    "Stock cannot be empty",
    "Name cannot contain special characters",
    "Price cannot be negative",
    "Stock cannot be negative"
    ]
    product_data={
        "name": name,
        "description": desc,
        "price": price,
        "stock": stock
    }
    response = log_response(client.post('/api/Product/', json=product_data), "Inserting data")
    assert response.status_code == 400
    assert response.json in [{'error': msg} for msg in expected_errors]

#PRUEBA 4
#LETRAS Y CARACTERES (PRECIO)
def test_invalidInputPrice_insert_product(client):
    product_data = {
        "name": "CocaCola",
        "description": "lorem ipsum",
        "price": "100.00"+"AB",
        "stock": 100
    }
    print("Sending data:", product_data)

    response = client.post('/api/Product/', json=product_data)


    print("Status Code:", response.status_code)
    print("Response Data:", response.data)
    print("Response Headers:", response.headers)

    assert response.status_code == 400
    data = json.loads(response.data)
    if data['message']['price']=='Price cannot be blank':
        message='Price must be a number'
    print("Message:", message)
    assert message == 'Price must be a number'

#PRUEBA 5
#LETRAS Y CARACTERES (STOCK)
def test_invalidInputStock_insert_product(client):
    product_data = {
        "name": "CocaCola",
        "description": "lorem ipsum",
        "price": 100,
        "stock": "100"+"AB"
    }
    print("Sending data:", product_data)

    response = client.post('/api/Product/', json=product_data)


    print("Status Code:", response.status_code)
    print("Response Data:", response.data)
    print("Response Headers:", response.headers)

    assert response.status_code == 400
    data = json.loads(response.data)
    if data['message']['stock']=='Stock cannot be blank':
        message='Stock must be a number'
    print("Message:", message)
    assert message == 'Stock must be a number'


#PRUEBA 5
#INSERTAR(put)PRODUCTO CON DESCRIPCION FUERA DE LIMITES
@pytest.mark.parametrize("name,desc,price,stock",[
    ("CocaCola", "Coquita", "100", "100"),
    ("CocaCola", "lorem"*1000, "100", "100")
])
def test_invalidDescRange_insert_product(client, name, desc, price, stock):
    expected_errors = [
    "Description must be at least 10 characters long",
    "Description cannot be longer than 1000 characters"
    ]
    product_data={
        "name": name,
        "description": desc,
        "price": price,
        "stock": stock
    }
    response = log_response(client.post('/api/Product/', json=product_data), "Inserting data")
    assert response.status_code == 400
    assert response.json in [{'error': msg} for msg in expected_errors]

#PRUEBA 6
#PRODUCTO YA EXISTENTE
@pytest.mark.parametrize("product_data",[
    product_test_data[0],
    product_test_data[0],
])
def test_insert_product_existing(client, product_data):
    response = log_response(client.post('/api/Product/', json=product_data), "Inserting data")
    assert response.status_code == 201
    assert len(response.json) == 1
    response = log_response(client.post('/api/Product/', json=product_data), "Inserting data")
    assert response.status_code == 400
    assert response.json == {'error': 'Name already exists'}
    
#PRUEBA 7
#MODIFICAR UN PRODUCTO Y PONER NOMBRE REPETIDO
@pytest.mark.parametrize("name,desc,price,stock",[
    (["CocaCola","Pepesi","CocaCola"],
    ["Coquita sabrosona","Pepesi medio meh","Pepesi medio meh"],
    [100,100,100],
    [100,100,100])
])
def test_update_product_existing_name(client,name,desc,price,stock):
   product_data={
       "name": name[0],
       "description": desc[0],
       "price": price[0],
       "stock": stock[0]
   }
   product_data2={
       "name": name[1],
       "description": desc[1],
       "price": price[1],
       "stock": stock[1]
   }
   response = log_response(client.post('/api/Product/', json=product_data), "Inserting data")
   assert response.status_code == 201
   response = log_response(client.post('/api/Product/', json=product_data2), "Inserting data")
   assert response.status_code == 201
   response = log_response(client.put('/api/Product/2', json=product_data), "Updating data")
   assert response.status_code == 400

#PRUEBA 8
#ACCEDER, MODIFICAR O ELIMINAR PRODUCTO INEXISTENTE
def test_access_update_delete_product_inexistent(client):
    
    response1 = log_response(client.put('/api/Product/2', json=product_test_data[0]), "Updating data")
    response2 = log_response(client.delete('/api/Product/2'), "Deleting data")    
    response3 = log_response(client.get('/api/Product/2'), "Accessing data")
    
    responses=[response1,response2,response3]

    for response in responses:
        assert response.status_code == 404
        assert response.json == {'error': 'Product not found'}
    
#PRUEBA 9
#ELIMINAR PRODUCTO
def test_delete_product(client):
    respose = log_response(client.post('/api/Product/', json=product_test_data[0]), "Inserting data")
    assert respose.status_code == 201
    response = log_response(client.delete('/api/Product/1'), "Deleting data")
    assert response.status_code == 200
    response = log_response(client.get('/api/Product/'), "Accessing data")
    assert response.status_code == 200
    assert response.json == []
    response = log_response(client.get('/api/Product/1'), "Accessing data")
    assert response.status_code == 404
    assert response.json == {'error': 'Product not found'}

#PRUEBA 10
#CREAR Y ACCEDER
def test_create_valid_product(client):
    response = log_response(client.post('/api/Product/', json=product_test_data[0]),"Sending data..")
    assert response.status_code == 201
    response = log_response(client.get('/api/Product/1'),"Accessing data")
    assert response.json['name'] == product_test_data[0]['name']
    assert len(response.json) == len(product_test_data[0]) + 1
    assert response.status_code == 200

#PRUEBA 11
#LISTAR PRODUCTOS
def test_get_products(client):
    for product in product_test_data:
        response = log_response(client.post('/api/Product/', json=product), "Sending data..")
        assert response.status_code == 201
    response = log_response(client.get('/api/Product/'), "Accessing data")
    assert response.status_code == 200
    assert len(response.json) == len(product_test_data)

#PRUEBA 12
#MODIFICAR PRODUCTO EXISTENTE Y VALIDAR LOS CAMBIOS
@pytest.mark.parametrize("product_data",[
    product_test_data[0],
    product_test_data[1],
])
def test_modify_product(client, product_data):
    response = log_response(client.post('/api/Product/', json=product_data), "Sending data..")
    assert response.status_code == 201
    response = log_response(client.put('/api/Product/1', json=product_test_data[2]), "Updating data")
    assert response.status_code == 200
    response = log_response(client.get('/api/Product/1'), "Accessing data")
    assert response.status_code == 200
    assert response.json['name'] == product_test_data[2]['name']
    assert response.json['description'] == product_test_data[2]['description']
    assert response.json['price'] == product_test_data[2]['price']
    assert response.json['stock'] == product_test_data[2]['stock']

#---------------------------------------FIN PRUEBAS PRODUCTO--------------------------------------------#

#-------------------------------------------PRUEBAS DEPTO-----------------------------------------------#
department_test_data = [
    {
        "nameDepartment": "Tecnologia",
        "description": "Departamento de Tecnologia",
        "user_id": 10
    },
    {
        "nameDepartment": "Telefonos",
        "description": "Departamento de Telefonos",
        "user_id": 9
    },
    {
        "nameDepartment": "Computadoras",
        "description": "Departamento de Computadoras",
        "user_id": 8
    }
]

#PRUEBA 1
#INSERTAR(post)DATOS NULOS/VACIOS
@pytest.mark.parametrize("name,desc,user_id",[
    (None, "Departamento de Tecnologia", 10),
    ("Tecnologia",None, 10),
    ("Tecnologia", "Departamento de Tecnologia", None)
])
def test_null_fields_insert_department(client,name,desc,user_id):
    department_data = {
        "nameDepartment": name,
        "description": desc,
        "user_id": user_id
    }
    response =log_response(client.post('/api/Department/', json=department_data), "Sending data..")
    assert response.status_code == 400
    assert response.json == {'error': 'Name cannot be empty'} or response.json == {'error': 'Description cannot be empty'} or response.json == {'error': 'User ID cannot be empty'}

#PRUEBA 2
#INSERTAR(post)NOMBRE REPETIDO
def test_repeated_name_insert_department(client):
    response = log_response(client.post('/api/Department/', json=department_test_data[0]), "Sending data..")
    assert response.status_code == 201
    response = log_response(client.post('/api/Department/', json=department_test_data[0]), "Sending data..")
    assert response.status_code == 400
    assert response.json == {'error': 'Name already exists'}
    
#PRUEBA 3
#CARACTERES INVALIDOS
@pytest.mark.parametrize("name,desc",[
    ("Tecnologia@", "Departamento de Tecnologia"),
    ("Tecnologia", "Departamento de Tecnologia@")
])
def test_invalid_caracters_insert_department(client,name,desc):
    department_data = {
        "nameDepartment": name,
        "description": desc,
        "user_id": 10
    }
    response = log_response(client.post('/api/Department/', json=department_data), "Sending data..")
    assert response.status_code == 400
    assert response.json == {'error': 'Name cannot contain special characters'} or response.json == {'error': 'Description cannot contain special characters'}

#PRUEBA 4
#TAMAÑO DE DESCRIPCION INVALIDO
@pytest.mark.parametrize("name,desc",[
    ("Tecnologia", "Dept"),
    ("Tecnologia", "Departamento de Tecnologia"*200)
])
def test_invalid_desc_len_department(client,name,desc):
    department_data={
        "nameDepartment": name,
        "description": desc,
        "user_id": 10
    }
    response = log_response(client.post('/api/Department/', json=department_data), "Sending data..")
    assert response.status_code == 400
    assert response.json == {'error': 'Description must be at least 10 characters long'} or response.json == {'error': 'Description cannot be longer than 1000 characters'}

#PRUEBA 5
#CREAR DEPARTAMENTO VALIDO
def test_create_valid_department(client):
    response =log_response(client.post('/api/Department/', json=department_test_data[0]), "Sending data..")
    assert response.status_code == 201
    assert len(response.json) == 1
    assert response.json[0]["nameDepartment"]==department_test_data[0]["nameDepartment"]
    
#PRUEBA 6
#OBTENER(get)LISTA VACIA
def test_get_empty_list_department(client):
    response = log_response(client.get('/api/Department/'), "Accessing data")
    assert response.status_code == 200
    assert response.json == []
    assert len(response.json) == 0

#PRUEBA 7
#OBTENER(get)LISTA CON ELEMENTOS
def test_get_list_department(client):
    for department in department_test_data:
        response = log_response(client.post('/api/Department/', json=department), "Sending data..")
        assert response.status_code == 201
    response = log_response(client.get('/api/Department/'), "Accessing data")
    assert response.status_code == 200
    assert len(response.json) == len(department_test_data)

    for i in range(len(response.json)):
        assert response.json[i]["nameDepartment"] == department_test_data[i]["nameDepartment"]
        assert response.json[i]["description"] == department_test_data[i]["description"]
        assert response.json[i]["user_id"] == department_test_data[i]["user_id"]
    
#PRUEBA 8
#OBTENER(get)UN ELEMENTO
def test_get_element_department(client):
    for department in department_test_data:
        response = log_response(client.post('/api/Department/', json=department), "Sending data..")
        assert response.status_code == 201
    
    response = log_response(client.get('/api/Department/2'), "Accessing data(department 2)")
    assert response.status_code == 200
    assert len(response.json)==len(department_test_data[1])+1
    assert response.json["nameDepartment"] == department_test_data[1]["nameDepartment"]
    assert response.json["description"] == department_test_data[1]["description"]
    assert response.json["user_id"] == department_test_data[1]["user_id"]

#PRUEBA 9
#OBTENER(get)UN ELEMENTO INEXISTENTE
def test_get_element_not_found_department(client):
    response = log_response(client.get('/api/Department/1'), "Accessing data(department 1)")
    assert response.status_code == 404
    assert response.json == {'error': 'Department not found'}

#PRUEBA 10
#EDITAR(put)DEPARTAMENTO INEXISTENTE
def test_edit_department_not_found(client):
    response = log_response(client.put('/api/Department/1', json=department_test_data[0]), "Updating data")
    assert response.status_code == 404
    assert response.json == {'error': 'Department not found'}
    
#PRUEBA 11
#EDITAR(put)CON DATOS VACIOS O INVALIDOS
@pytest.mark.parametrize("nameDpt,Desc,uId",[
    (None,"Departamento de Tecnologia","10"),
    ("Tecnologia",None,"10"),
    ("Tecnologia","Departamento de Tecnologia",None),
    ("Tecnologi@","Departamento de tecnologia","10"),
    ("Tecnologia","Departamento de tecnologi¿@","10"),
    ("Tecnologia", "12Departamento de tecnologia", "10")
])
def test_edit_department_empty_data(client,nameDpt,Desc,uId):
    expected_errors = [
    'Name cannot be empty',
    'Description cannot be empty',
    'User ID cannot be empty',
    'Description cannot contain special characters',
    'Description cannot contain numbers',
    'Name cannot contain special characters'
    ]
    department_data= {
        "nameDepartment": nameDpt,
        "description": Desc,
        "user_id": uId
    }
    response = log_response(client.post('/api/Department/', json=department_test_data[2]), "Sending data..")
    assert response.status_code == 201
    response = log_response(client.put('/api/Department/1', json=department_data), "Updating data")
    assert response.status_code == 400

    assert response.json in [{'error': msg} for msg in expected_errors]

#PRUEBA 12
#EDITAR(put) CON NOMBRE EXISTENTE
def test_edit_department_name_exists(client):
    for i in range(len(department_test_data)-1):
        response = log_response(client.post('/api/Department/', json=department_test_data[i]), "Sending data..")
        assert response.status_code == 201
    response = log_response(client.put('/api/Department/1', json=department_test_data[0]), "Updating data")
    assert response.json == {'error': 'Name already exists'}

#PRUEBA 13
#EDITAR (put) CON DATOS VALIDOS
def test_edit_department_valid_data(client):
    for i in range(len(department_test_data)-1):
        response = log_response(client.post('/api/Department/', json=department_test_data[i]), "Sending data..")
        assert response.status_code == 201

    response = log_response(client.put('/api/Department/1', json=department_test_data[2]), "Updating data")
    assert response.status_code == 200
    response = log_response(client.get('/api/Department/1'), "Accessing data(department 1)")
    assert response.status_code == 200
    assert response.json["nameDepartment"] == department_test_data[2]["nameDepartment"]
    assert response.json["description"] == department_test_data[2]["description"]
    assert response.json["user_id"] == department_test_data[2]["user_id"]

#PRUEBA 14
#ELIMINAR(delete)UN ELEMENTO INEXISTENTE
def test_delete_department_not_found(client):
    response = log_response(client.delete('/api/Department/1'), "Deleting data")
    assert response.status_code == 404
    assert response.json == {'error': 'Department not found'}

#PRUEBA 15
#ELIMINAR(delete)ELEMENTO CON EXITO
def test_delete_department(client):
    response = log_response(client.post('/api/Department/', json=department_test_data[0]), "Sending data..")
    assert response.status_code == 201
    assert len(response.json) == 1

    response = log_response(client.delete('/api/Department/1'), "Deleting data")
    assert response.status_code == 200
    assert len(response.json) == 0
    response= log_response(client.get('/api/Department/'),"Accessing data")
    assert response.status_code == 200
    assert len(response.json) == 0
    assert response.json == []



#PRUEBA 56
#OBTENER LAS ORDENES
def test_get_orders(client):
    response = client.get('/api/Order/')
    assert response.status_code == 200
    assert response.json == []

#PRUEBA 57
#AGREGAR UNA ORDEN
def test_userId__empty(client):
    response = client.post('/api/Order/', json={
        "userId": "",
        "orderDate": "2023-12-12",
        "total": 100,
        "status": "Pending"
    })
    assert response.status_code == 400

#PRUEBA 58
#VER ORDENES PRODUCTO
def test_get_orderProduct(client):
    response = client.get('/api/OrderProduct/')
    assert response.status_code == 200
    assert response.json == []

#PRUEBA 59
#NO PUEDE IR VACIO LA ORDEN ID
def test_orderId__empty(client):
    response = client.post('/api/OrderProduct/', json={
        "orderId": "",
        "productId": 1,
        "quantity": 1
    })
    assert response.status_code == 400

#PRUEBA 60
#NO PUEDE IR VACIO EL PRODUCTO ID
def test_productId__empty(client):
    response = client.post('/api/OrderProduct/', json={
        "orderId": 1,
        "productId": "",
        "quantity": 1
    })
    assert response.status_code == 400

#PRUEBA 61
#NO PUEDE IR VACIO LA CANTIDAD
def test_quantity__empty(client):
    response = client.post('/api/OrderProduct/', json={
        "orderId": 1,
        "productId": 1,
        "quantity": ""
    })
    assert response.status_code == 400


#PRUEBA 62
#SOLO EXISTE UNA order_id en ORDENES PRODUCTOS
def test_orderId__unique(client):
    response = client.post('/api/OrderProduct/', json={
        "orderId": 1,
        "productId": 1,
        "quantity": 1
    })
    assert response.status_code == 400 