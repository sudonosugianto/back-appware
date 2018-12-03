from flask import Flask, render_template
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from functools import wraps
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://appware@appware.cqca0rvctn3a.ap-southeast-1.rds.amazonaws.com:3306/appware'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://appware:password@appware.cqca0rvctn3a.ap-southeast-1.rds.amazonaws.com/appware"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:020601@127.0.0.1/AppWare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JWT_SECRET_KEY'] = 'AppwareSecretKey'
CORS(app)
api = Api(app)
jwt = JWTManager(app)

from models import db
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from modelUsers import Users

@jwt.expired_token_loader
def exipred_token_message():
    return json.dumps({"message": "The token has expired"}), 401, {'Content-Type': 'application/json'}

@jwt.user_claims_loader
def add_claims(identity) :
    qry = Users.query.filter_by(id=identity).first()
    id = qry.id
    return {
        'id' : id
    }

@jwt.unauthorized_loader
def unathorized_message(error_string):
    return json.dumps({'message': error_string}), 401, {'Content-Type': 'application/json'}

# Page Untuk Halaman Home

# @app.route("/")
# def webprint():
#     return render_template('docs/index.html')