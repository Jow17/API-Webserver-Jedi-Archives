from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from os import environ
from marshmallow.exceptions import ValidationError

app = Flask(__name__)

app.json.sort_keys = False

# Retrieves key and DB_URI connection string from .env for database security
app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = environ.get('DB_URI')

# Creates instances of objects to be used in the app
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Error handling in JSON format
@app.errorhandler(401)
def unauthorized(err):
    return {'error': 'You are not authorized to access this resource'}

@app.errorhandler(ValidationError)
def validation_error(err):
    return {'error': err.messages}