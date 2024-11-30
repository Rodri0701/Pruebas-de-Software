from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from api.controllers import User, Users
from api.models import UserModel,db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()
    
api.add_resource(Users, "/api/users/")
api.add_resource(User, "/api/users/<int:user_id>")

@app.route("/")
def hello_world():
    return "<h1> Hello, World! </h1>"

if __name__ == "__main__":
    app.run(debug=True)