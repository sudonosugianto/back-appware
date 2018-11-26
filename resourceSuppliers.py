from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime
# or_ untuk search lebih dari 1 kolom
from sqlalchemy import or_

from models import db
####### Tempat import Model#########
from modelSuppliers import Suppliers
####### Finish import Model#########


####### Tempat import Marshal#########
from marshalField import supplier_fields
####### Finish import Marshal#########

class SupplierResources(Resource):

    # Untuk tambah suppliers
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, location="json", required=True, help="name must be String")
        parser.add_argument("phone_number", type=str, location="json", required=True, help="phone_number must be string")
        parser.add_argument("email", type=str, location="json", required=False, help="email must be string")
        parser.add_argument("address", type=str, location="json", required=False, help="address must be string")
        parser.add_argument("city", type=str, location="json", required=False, help="city must be string")
        parser.add_argument("state", type=str, location="json", required=False, help="state must be string")
        parser.add_argument("zipcode", type=str, location="json", required=False, help="zipcode must be string")

        args = parser.parse_args()
        my_identity = get_jwt_identity()

        add_supplier = Suppliers(
            userSuppliersID = my_identity,
            name = args['name'],
            phone_number = args['phone_number'],
            email= args['email'],
            address = args['address'],
            city = args['city'],
            state= args['state'],
            zipcode=args['zipcode']
        )

        db.session.add(add_supplier)
        db.session.commit()
        
        return {
            "message": "add supplier success",
            "supplier": marshal(add_supplier, supplier_fields)
        }, 200

    # untuk edit Suppliers
    @jwt_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, location="json", required=True, help="name must be String")
        parser.add_argument("phone_number", type=str, location="json", required=True, help="phone_number must be string")
        parser.add_argument("email", type=str, location="json", required=False, help="email must be string")
        parser.add_argument("address", type=str, location="json", required=False, help="address must be string")
        parser.add_argument("city", type=str, location="json", required=False, help="city must be string")
        parser.add_argument("state", type=str, location="json", required=False, help="state must be string")
        parser.add_argument("zipcode", type=str, location="json", required=False, help="zipcode must be string")
        args = parser.parse_args()
        
        qry = Suppliers.query.filter_by(id = id).first()
        
        if qry == None :
            return {'message': 'suppliers not found'}, 404

        else:
            if args["name"] != None:
                qry.name= args["name"]
            if args["phone_number"] != None:
                qry.phone_number= args["phone_number"]
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
                "message": "edit supplier success",
                "product": marshal(qry, supplier_fields)
            } ,200

    # Untuk hapus suppliers
    @jwt_required
    def delete(self, id):
        qry = Suppliers.query.filter_by(id = id).first()

        if qry == None:
            return {'message': "supplier not found!"}, 404

        db.session.delete(qry)
        db.session.commit()

        return {'message': "delete supplier success"}, 200

    # Untuk menampilkan supplier
    @jwt_required
    def get(self, id=None):
        my_identity = get_jwt_identity()

        qry = Suppliers.query

        #   get by id

        if id != None:
            qry = qry.filter_by(userSuppliersID = my_identity).filter_by(id = id)

            rows = []

            for row in qry.all():
                rows.append(marshal(row, supplier_fields))

            if rows == []:
                return {'message': 'supplier not found'}, 404

            return {
                "message": "success",
                "package": rows
            }, 200
            
        parser = reqparse.RequestParser()
        parser.add_argument("search", type=str, location="args", help="Search must be string")
        args = parser.parse_args()

        qry = Suppliers.query.filter_by(userSuppliersID = my_identity)
        
        if args['search'] is not None:
            search = args['search']
            # Fungsi untuk search, digunakan filter daripada filter_by 
            # karena butuh method like dengan regex %
            qry = qry.filter(or_(Suppliers.name.like('%'+search+'%'),\
                                 Suppliers.address.like('%'+search+'%'),\
                                 Suppliers.phone_number.like('%'+search+'%'),\
                                 Suppliers.email.like('%'+search+'%')   )).all()
        else:
            qry = qry.all()
        
        if marshal(qry,supplier_fields) == [] :
            return {"message": "You doesn't have any suppliers"}, 404
        
        return {
            "message": "success",
            "supplier": marshal(qry,supplier_fields)
        }, 200