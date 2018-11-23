from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request

from models import db
####### Tempat import Model#########
from modelUsers import Users
####### Finish import Model#########

####### Tempat import Model#########
from marshalField import user_field
####### Finish import Model#########

class User(Resource):
    pass