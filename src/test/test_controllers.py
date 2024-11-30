import pytest
from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from api.models import db, UserModel
from api.controllers import User, Users
from unittest.mock import patch, Mock, MagicMock
from flask_restful import Api
import unittest

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = True
    db.init_app(app)
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_user_get_not_found(client):
    response = client.get('/users/999')
    assert response.status_code == 404
    
def test_verify_email(client):
    mock_users_repository = MagicMock()
    mock_users_repository.get_all.return_value = {
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
            "toxic": "unknown"
        }      
    assert mock_users_repository.get_all.return_value['status'] == 'deliverable'
    assert mock_users_repository.get_all.return_value['reason'] == 'accepted_email'

@patch.object(User, 'get')
def test_user_get(mock_get):
    mock_user = Mock()
    mock_user.id = 1
    mock_user.username = 'xxxxxxxxxx'
    mock_user.email = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    mock_get.return_value = mock_user

    result = User.get()
    assert result == mock_user
    assert result.id == 1
    assert result.username == 'xxxxxxxxxx'
    assert result.email == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    mock_get.assert_called_once()

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'slite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.api = Api(self.app)
        self.api.add_resource(Users, '/users/<int:user_id>')
        self.client = self.app.test_client()

        self.app_context = self.app.app_context()
        self.app_context.push()

        db.init_app(self.app)
        db.create_all()

    @patch('api.controllers.UserModel.query')
    def test_get_user(self, mock_querry):
        mock_querry.filter_by.return_value.firts.return_vaule = UserModel(id = 1, username = 'test', email = 'test@test.com')
        response = self.client.get('/user/1')

        self.assertEqual(response.status.code, 200)
        self.assertIn('test',response.get_data(as_text=True))