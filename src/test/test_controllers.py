from flask.testing import FlaskClient
import pytest
import unittest
from flask import Flask,json
from api.models import db, UserModel,ProductModel,OrderModel,OrderProductModel,DepartmentModel
from api.controllers import User, Users, Product, Products, Order, Orders, Department, Departments, OrderProduct, OrdersProducts
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource,reqparse
from unittest.mock import patch, MagicMock, Mock



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
