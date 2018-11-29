from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime

from models import db
####### Tempat import Model#########
from modelUsers import Users
####### Finish import Model#########

####### Tempat import Model#########
from marshalField import user_fields
####### Finish import Model#########

# class User(Resource):
#     pass

class LoginResources(Resource):

    # Untuk register user
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str, location="json", required=True, help="email must be string and exist")
        parser.add_argument("password", type=str, location="json", required=True, help="password must be string and exist")

        args = parser.parse_args()

        qry = Users.query.filter_by(email=args['email'], password=args['password']).first()

        if qry == None:
            return {'message': 'unauthorized'}, 401

        # token = create_access_token(identity= qry.id, expires_delta=datetime.timedelta(days=30))
        token = create_access_token(identity= qry.id, expires_delta= datetime.timedelta(days=30))

        return {
            "message": "login success",
            "token": token,
            "user": marshal(qry, user_fields)
        }, 200