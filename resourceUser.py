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

class UserResources(Resource):

    # Untuk register user
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("fullname", type=str, location="json", required=True, help="fullname must be string and exist")
        parser.add_argument("username", type=str, location="json", required=True, help="username must be string and exist")
        parser.add_argument("password", type=str, location="json", required=True, help="password must be string and exist")
        parser.add_argument("email", type=str, location="json", required=True, help="email must be string and exist")
        parser.add_argument("phone_number", type=str, location="json", required=True, help="phone_number must be string")

        args = parser.parse_args()

        qry1 = Users.query.filter_by(username=args["username"]).first()
        qry2 = Users.query.filter_by(email=args["email"]).first()

        if qry1 != None or qry2 != None:
            return {"message": "username or email has been used"}, 403

        add_user = Users(
            fullname = args['fullname'],
            username = args['username'],
            password= args['password'],
            email= args['email'],
            phone_number= args['phone_number']
        )

        db.session.add(add_user)
        db.session.commit()

        # create token
        token = create_access_token(identity= add_user.id, expires_delta=datetime.timedelta(days=30))
        
        return {
            "message": "registration success",
            "token": token,
            "user": marshal(add_user, user_fields)
        }, 200