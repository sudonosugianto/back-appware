from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request


from models import db
####### Tempat import Model#########
from modelPO import PO
from modelSuppliers import Suppliers
from modelStocks import Stocks
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

        qrystocks = Stocks.query.join(Packages, Stocks.packagesID == Packages.id)\
                                .filter(Packages.userPackageID == my_identity ).all()
        
        # Script get the StockID per User via UserPackageID
        # Output File tmp_suppliers nantinya [1,3, ..etc]
        tmp_stocks = []
        for item in qrystocks:
            tmp_stocks.append(item.id)
        
        parser = reqparse.RequestParser()
        # Package ID diberikan choices hanya ID yang dimiliki user
        parser.add_argument('supplierID', type = int, help='You\'re pick a wrong choice of Supplier ID', location='json', choices=tmp_suppliers)
        parser.add_argument('stockID', type = int, help='You\'re pick a wrong choice of Stock ID', location='json',choices=tmp_stocks)
        parser.add_argument('notes', type = str, help='Write Note for Remind you something.', location='json')
        args = parser.parse_args()

        add_po = PO(
            supplierID = args['supplierID'],
            stockID = args['stockID'],
            notes = args['notes']
        )
        
        qry = PO.query.filter_by(supplierID=args['supplierID'],stockID=args['stockID']).first()
        
        db.session.add(add_po)
        db.session.commit()

        return {
            "message": "Add Initiate Stock Success",
            "supplier": marshal(qrysupplier,{'id':fields.Integer,\
                                            'name':fields.String}),
            "stock": marshal(qrystocks,{'id':fields.Integer}),
            "PO": marshal(qry, po_fields)
        } ,200