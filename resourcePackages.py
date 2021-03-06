from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime
from sqlalchemy import or_, desc

from models import db
####### Tempat import Model#########
from modelPackages import Packages
from modelItems import Items
from modelCat import Category
####### Finish import Model#########


####### Tempat import Marshal#########
from marshalField import package_fields
from marshalField import item_fields
####### Finish import Marshal#########

class PackageResources(Resource):

    # Untuk tambah package
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("itemID", type=int, location="json", required=True, help="itemID must be integer and exist")
        parser.add_argument("package_name", type=str, location="json", required=True, help="package_name must be string and exist")
        parser.add_argument("items_quantity", type=int, location="json", required=False, help="items_quantity must be integer")

        args = parser.parse_args()
        my_identity = get_jwt_identity()

        add_package = Packages(
            catPackageID = marshal(Items.query.filter_by(id=args["itemID"]).first(), item_fields)["catID"],
            userPackageID = my_identity,
            itemID = args['itemID'],
            package_name = args['package_name'],
            items_quantity= args['items_quantity']
        )

        db.session.add(add_package)
        db.session.commit()
        
        return {
            "message": "add package success",
            "package": marshal(add_package, package_fields)
        }, 200

    # untuk edit package
    @jwt_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('itemID', type = int, help='itemID must be integer type', location='json')
        parser.add_argument('package_name', type = str, help='package_name must be string type', location='json')
        parser.add_argument('items_quantity', type = int, help='items_quantity must be string type', location='json')

        args = parser.parse_args()
        
        qry = Packages.query.filter_by(id = id).first()
        
        if qry == None :
            return {'message': 'package not found'}, 404

        else:
            if args["itemID"] != None:
                qry.itemID= args["itemID"]
            if args["package_name"] != None:
                qry.package_name= args["package_name"]
            if args["items_quantity"] != None:
                qry.items_quantity= args["items_quantity"]

            qry.updated_at = db.func.current_timestamp()
                    
            db.session.add(qry)
            db.session.commit()

            return {
                "message": "edit package success",
                "product": marshal(qry, package_fields)
            } ,200

    # Untuk hapus package
    @jwt_required
    def delete(self, id):
        
        qry = Packages.query.filter_by(id = id).first()

        if qry == None:
            return {'message': "package not found!"}, 404

        db.session.delete(qry)
        db.session.commit()

        return {'message': "delete package success"}, 200

    # Untuk menampilkan package
    @jwt_required
    def get(self, id=None):

        my_identity = get_jwt_identity()

        qry = Packages.query.join(Items, Items.id == Packages.itemID)\
                                .filter(Packages.userPackageID == my_identity).order_by(Packages.package_name)

        #   get by id

        if id != None:
            qry = qry.filter(Packages.id == id)

            rows = []

            for row in qry.all():
                rows.append(marshal(row, package_fields))

            if rows == []:
                return {'message': 'package not found'}, 404

            return {
                "message": "success",
                "package": rows
            }, 200

        # get all

        parser=reqparse.RequestParser()
        parser.add_argument('search',type=str,location='args')
        args=parser.parse_args()

        if args['search'] is not None:
                search = args["search"]
                qry = qry.filter(or_(Packages.package_name.like('%'+search+'%'),Items.item.like('%'+search+'%')))\
                                .order_by(Packages.package_name)

        rows = []

        for row in qry.all():
            rows.append(marshal(row, package_fields))

        if rows == []:
            return {'message': 'package not found'}, 404

        return {
            "message": "success",
            "packages": rows
        }, 200