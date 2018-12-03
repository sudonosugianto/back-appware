from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from models import db
####### Tempat import Model#########
from modelUsers import Users
####### Finish import Model#########


####### Tempat import Marshal#########
from marshalField import user_fields
####### Finish import Marshal#########


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
            return {"message": "username or email has been used"}, 400

        add_user = Users(
            fullname = args['fullname'],
            username = args['username'],
            password= generate_password_hash(args["password"]),
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

    # untuk edit profil user
    @jwt_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('fullname', type = str, help='fullname must be string type', location='json')
        parser.add_argument('username', type = str, help='username must be string type', location='json')
        parser.add_argument('password', type = str, help='password must be string type', location='json')
        parser.add_argument('email', type = str, help='email must be string type', location='json')
        parser.add_argument('phone_number', type = str, help='phone_number status must be string type',location='json')

        args = parser.parse_args()

        my_identity = get_jwt_identity()
        
        qry = Users.query.filter_by(id = my_identity).first()
        
        if qry == None :
            return {'message': 'user not found'}, 404

        qry1 = Users.query.filter_by(username = args["username"]).first()
        qry2 = Users.query.filter_by(email = args["email"]).first()        

        if qry1 != None or qry2 != None:
            return {"message": "username or email has been used"}, 400
            
        else:
            if args["fullname"] != None:
                qry.fullname= args["fullname"]
            if args["username"] != None:
                qry.username= args["username"]
            if args["password"] != None:
                qry.password= generate_password_hash(args["password"]),
            if args["email"] != None:
                qry.email= args["email"]
            if args["phone_number"] != None:
                qry.phone_number= args["phone_number"]

            qry.updated_at = db.func.current_timestamp()
                    
            db.session.add(qry)
            db.session.commit()
            return {
                "message": "edit profil success",
                "product": marshal(qry, user_fields)
            } ,200

    @jwt_required
    def delete(self, id):
        my_identity = get_jwt_identity()
        
        qry = Users.query.filter_by(id = my_identity).first()

        if qry == None:
            return {'message': "user not found!"}, 404

        db.session.delete(qry)
        db.session.commit()

        return {'message': "delete user success"}, 200

    @jwt_required
    def get(self):

        my_identity = get_jwt_identity()

        qry = Users.query.filter_by(id = my_identity)

        rows = []

        for row in qry.all():
            rows.append(marshal(row, user_fields))

        if rows == []:
            return {'message': 'user not found'}, 404

        return {
            "message": "success",
            "user": rows
        }, 200