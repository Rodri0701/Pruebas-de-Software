from flask.testing import FlaskClient
import pytest
from flask import Flask,json
from api.models import db, UserModel,ProductModel,OrderModel,OrderProductModel,DepartmentModel
from api.controllers import User, Users, Product, Products, Order, Orders, Department, Departments, OrderProduct, OrdersProducts
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource,reqparse
from unittest.mock import patch, MagicMock, Mock
import unittest


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
    response = client.post('/api/User/', json={
        "username": " ",
        "password": "contrasegura",
        "email": "sadfjkn@gmail.com",
        "phone": 1234567981,
        "address": "sfhdsf #44",
        "role": "Employee"
    })
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'field' in data
    assert data['field'] == 'username'
    
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

     

