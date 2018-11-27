from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime


from models import db


####### Tempat import Model#########
from modelCustomers import Customers
####### Finish import Model#########


####### Tempat import Marshal#########
from marshalField import customer_fields
####### Finish import Marshal#########


class CustomerResources(Resource):

    # Untuk tambah customer
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("fullname", type=str, location="json", required=True, help="fullname must be string and exist")
        parser.add_argument("phoneNumber", type=str, location="json", required=True, help="phoneNumber must be string and exist")
        parser.add_argument("email", type=str, location="json", required=True, help="email must be string and exist")
        parser.add_argument("address", type=str, location="json", help="address must be string")
        parser.add_argument("city", type=str, location="json", help="city must be string")
        parser.add_argument("state", type=str, location="json", help="state must be string")
        parser.add_argument("zipcode", type=str, location="json", help="zipcode must be string")

        args = parser.parse_args()

        my_identity = get_jwt_identity()

        qry1 = Customers.query.filter_by(phoneNumber=args["phoneNumber"]).first()
        qry2 = Customers.query.filter_by(email=args["email"]).first()

        if qry1 != None or qry2 != None:
            return {"message": "phoneNumber or email has been used"}, 400

        add_customer = Customers(
            userCustomerID = my_identity,
            fullname = args['fullname'],
            phoneNumber= args['phoneNumber'],
            email= args['email'],
            address = args['address'],
            city= args['city'],
            state= args['state'],
            zipcode= args['zipcode']
        )

        db.session.add(add_customer)
        db.session.commit()
        
        return {
            "message": "add customer success",
            "customer": marshal(add_customer, customer_fields)
        }, 200

    # untuk edit profil customer
    @jwt_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('fullname', type = str, help='fullname must be string type', location='json')
        parser.add_argument('phoneNumber', type = int, help='phoneNumber status must be string type',location='json')
        parser.add_argument('email', type = str, help='email must be string type', location='json')
        parser.add_argument('address', type = str, help='address must be string type', location='json')
        parser.add_argument('city', type = str, help='city must be string type', location='json')
        parser.add_argument('state', type = str, help='state must be string type', location='json')
        parser.add_argument('zipcode', type = str, help='zipcode must be string type', location='json')

        args = parser.parse_args()

        my_identity = get_jwt_identity()
        
        qry = Customers.query.filter_by(userCustomerID = my_identity).filter_by(id = id).first()
        
        if qry == None :
            return {'message': 'customer not found'}, 404

        else:
            if args["fullname"] != None:
                qry.fullname= args["fullname"]
            if args["phoneNumber"] != None:
                qry.phoneNumber= args["phoneNumber"]
            if args["email"] != None:
                qry.email= args["email"]
            if args["address"] != None:
                qry.address= args["address"]
            if args["city"] != None:
                qry.city= args["city"]
            if args["state"] != None:
                qry.state= args["state"]
            if args["zipcode"] != None:
                qry.zipcode= args["zipcode"]

            qry.updated_at = db.func.current_timestamp()
                    
            db.session.add(qry)
            db.session.commit()

            return {
                "message": "edit customer success",
                "customer": marshal(qry, customer_fields)
            } ,200

    @jwt_required
    def delete(self, id):

        my_identity = get_jwt_identity()
        
        qry = Customers.query.filter_by(userCustomerID = my_identity).filter_by(id = id).first()

        if qry == None:
            return {'message': "customer not found!"}, 404

        db.session.delete(qry)
        db.session.commit()

        return {'message': "delete customer success"}, 200

    # menampilkan customer
    @jwt_required
    def get(self, id=None):

        my_identity = get_jwt_identity()

        qry = Customers.query

        #   get by id

        if id != None:
            qry = qry.filter_by(userCustomerID = my_identity).filter_by(id = id)

            rows = []

            for row in qry.all():
                rows.append(marshal(row, customer_fields))

            if rows == []:
                return {'message': 'customer not found'}, 404

            return {
                "message": "success",
                "customer": rows
            }, 200

        # get all

        qry = Customers.query.filter_by(userCustomerID = my_identity)

        rows = []

        for row in qry.all():
            rows.append(marshal(row, customer_fields))

        if rows == []:
            return {'message': 'customer not found'}, 404

        return {
            "message": "success",
            "customers": rows
        }, 200