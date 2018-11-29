from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
from sqlalchemy import desc, between, and_, or_
from datetime import datetime

from models import db
####### Tempat import Model#########
from modelPO import PO
from modelSuppliers import Suppliers
from modelPackages import Packages
####### Finish import Model#########

####### Tempat import Model#########
from marshalField import po_fields
####### Finish import Model#########

class POResources(Resource):
    # Untuk Create Item
    @jwt_required
    def post(self):
        my_identity = get_jwt_identity()
        
        qrysupplier = Suppliers.query.filter_by(userSuppliersID = my_identity).all()
        # Script get the SupplierID per User
        # Output File tmp_suppliers nantinya [1,3, ..etc]
        tmp_suppliers = []
        for item in qrysupplier:
            tmp_suppliers.append(item.id)
        
        qrypackage = Packages.query.filter_by(userPackageID = my_identity).all()
        # Script get the PackageID per User
        # Output File tmp_package nantinya [1,3, ..etc]
        tmp_package = []
        for item in qrypackage:
            tmp_package.append(item.id)

        
        parser = reqparse.RequestParser()
        # Package ID diberikan choices hanya ID yang dimiliki user
        parser.add_argument('supplierID', type = int, help='You\'re pick a wrong choice of Supplier ID', location='json', choices=tmp_suppliers)
        parser.add_argument('packagePOID', type = int, help='You\'re pick a wrong choice of Supplier ID', location='json', choices=tmp_package)
        parser.add_argument('quantity', type = int, help='Quantity must be Integer', required=True)
        parser.add_argument('buyingPricePerPackage', type=float, help='price buy cost per package', required=True)
        parser.add_argument('notes', type = str, help='Give a notes for this PO')
        args = parser.parse_args()

        # Perhitungan harga total pembelian
        totalPrice = float(args['quantity'])* args['buyingPricePerPackage']
        add_po = PO(
            supplierID = args['supplierID'],
            userPOID = my_identity,
            packagePOID = args['packagePOID'],
            quantity = args['quantity'],
            buyingPricePerPackage = args['buyingPricePerPackage'],
            totalPrice = totalPrice,            
            notes = args['notes']
        )

        db.session.add(add_po)
        db.session.commit()

        # qry untuk mendapatkan post PO terakhir oleh user
        qry = PO.query.filter_by(userPOID=my_identity).order_by(desc(PO.created_at)).first()

        return {
            "message": "Add PO Success",
            "PO": marshal(qry, po_fields)
        } ,200

        # Update PO
    @jwt_required
    def put(self,id=None):
        parser = reqparse.RequestParser()
        parser.add_argument('supplierID', type = int, help='You\'re pick a wrong choice of Supplier ID', location='json')
        parser.add_argument('packagePOID', type = int, help='You\'re pick a wrong choice of Supplier ID', location='json')
        parser.add_argument('quantity', type = int, help='Quantity must be Integer', required=True)
        parser.add_argument('buyingPricePerPackage', type=float, help='price buy cost per package', required=True)
        args = parser.parse_args()

        my_identity = get_jwt_identity()

        qry = PO.query.filter_by(userPOID = my_identity).filter_by(id = id).first()

        if qry == None :
            return {'message': 'Purchase Order not found'}, 404

        else:
            if args["supplierID"] != None:
                qry.supplierID= args["supplierID"]
            if args["packagePOID"] != None:
                qry.packagePOID= args["packagePOID"]
            if args["quantity"] != None:
                qry.quantity= args["quantity"]
            if args["buyingPricePerpackage"] != None:
                qry.buyingPricePerpackage= args["buyingPricePerpackage"]

        qry.updated_at = db.func.current_timestamp()

        db.session.add(qry)
        db.session.commit()

        return {
            "message": "Edit purchase order success",
            "sale": marshal(qry, po_fields)
        } ,200

    # Delete Purchase Order
    @jwt_required
    def delete(self, id=None):
        my_identity = get_jwt_identity()
        qry = PO.query.filter_by(userPOID = my_identity).filter_by(id = id).first()
        if qry == None:
            return {'message': "sale not found!"}, 404

        db.session.delete(qry)
        db.session.commit()

        return {'message': "delete sale success"}, 200

    @jwt_required
    def get(self,id=None):
        my_identity = get_jwt_identity()

        parser = reqparse.RequestParser()
        parser.add_argument("dateStart", type=str, location="args", help="Date Time must be in format YYYY-MM-DD HH:MM:SS")
        parser.add_argument("dateEnd", type=str, location="args", help="Date Time must be in format YYYY-MM-DD HH:MM:SS")
        args = parser.parse_args()

        # dateStart = datetime.strptime(args['dateStart'], '%Y-%m-%d %H:%M:%S')
        # dateEnd = datetime.strptime(args['dateEnd'], '%Y-%m-%d %H:%M:%S')
        dateStart = args['dateStart']
        dateEnd = args['dateEnd']

        qry = PO.query.filter_by(userPOID = my_identity)

        # Filter by date
        if args['dateStart'] != None and args['dateEnd'] != None:
            qry = qry.filter(and_(PO.created_at >= dateStart, PO.created_at <= dateEnd))

        rows = []
        #   get by id
        if id != None:
            qry = qry.filter_by(id = id)

            for row in qry.all():
                rows.append(marshal(row, po_fields))

            if rows == []:
                return {'message': 'po not found'}, 404

            return {
                "message": "success",
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "PO": rows
            }, 200
        else:
            # get all
            for row in qry.all():
                rows.append(marshal(row, po_fields))

            if rows == []:
                return {'message': 'sale not found'}, 404

            return {
                "message": "success",
                "dateStart": dateStart,
                "dateEnd": dateEnd,
                "PO": rows
            }, 200
