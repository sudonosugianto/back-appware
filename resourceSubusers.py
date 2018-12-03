from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime
from strgen import StringGenerator
# from werkzeug.security import generate_password_hash

from models import db

####### Tempat import Model#########
from modelSubusers import Subusers
####### Finish import Model#########


####### Tempat import Marshal#########
from marshalField import subuser_fields
####### Finish import Marshal#########


class SubuserResources(Resource):

    # Untuk tambah subusers
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("fullname", type=str, location="json", required=True, help="fullname must be string and exist")
        parser.add_argument("email", type=str, location="json", required=True, help="email must be string and exist")
        parser.add_argument("username", type=str, location="json", required=True, help="username must be string and exist")
        parser.add_argument("phone_number", type=str, location="json", required=True, help="phone_number must be string")
        parser.add_argument("subuser_type", type=str, location="json", required=True, help="subuser_type must be string")
        args = parser.parse_args()

        my_identity = get_jwt_identity()
        concate = StringGenerator('[a-zA-Z0-9_]').render_list(32,unique=True)
        add_subuser = Subusers(
            userID = my_identity,
            fullname = args['fullname'],
            email= args['email'],
            username = args['username'],
            apiKey = ''.join(concate),
            phone_number= args['phone_number'],
            subuser_type= args['subuser_type']
        )

        db.session.add(add_subuser)
        db.session.commit()

        # create token
        token = create_access_token(identity= add_subuser.id, expires_delta=datetime.timedelta(days=30))
        
        return {
            "message": "add subuser success",
            "token": token,
            "user": marshal(add_subuser, subuser_fields)
        }, 200


    @jwt_required
    def get(self):

        my_identity = get_jwt_identity()

        qry = Subusers.query.filter(Subusers.userID == my_identity)

        rows = []

        for row in qry.all():
            rows.append(marshal(row, subuser_fields))

        if rows == []:
            return {'message': 'subuser not found'}, 404

        return {
            "message": "success",
            "subuser": rows
        }, 200