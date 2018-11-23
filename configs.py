from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://appware@appware.cqca0rvctn3a.ap-southeast-1.rds.amazonaws.com:3306/appware'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://appware:password@appware.cqca0rvctn3a.ap-southeast-1.rds.amazonaws.com/appware"
app.config['JWT_SECRET_KEY'] = 'AppwareSecretKey'
api = Api(app)
jwt = JWTManager(app)

from models import db
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)