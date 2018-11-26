from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request


from models import db
####### Tempat import Model#########
from modelPO import PO
from modelPODetails import PODetails
from modelSuppliers import Suppliers
from modelStocks import Stocks
from modelPackages import Packages
####### Finish import Model#########

####### Tempat import Model#########
from marshalField import podetail_fields
####### Finish import Model#########

class PODetailResources(Resource):
    # Untuk Create Item
    @jwt_required
    def post(self):
        my_identity = get_jwt_identity()
        
        qrypo = PO.query.join(Stocks, PO.stockID == Stocks.id)\
                        .join(Packages, Stocks.packagesID == Packages.userPackageID)\
                        .filter(Packages.userPackageID == my_identity ).all()
        
        # Script get the POID per User
        # Output File tmp_po nantinya [1,3, ..etc]
        tmp_po = []
        for item in qrypo:
            tmp_po.append(item.id)

        qrypackage = Packages.query.filter(Packages.userPackageID == my_identity).all()
        
        # Script get the StockID per User via UserPackageID
        # Output File tmp_package nantinya [1,3, ..etc]
        tmp_package = []
        for item in qrypackage:
            tmp_package.append(item.id)
        
        parser = reqparse.RequestParser()
        # Package ID diberikan choices hanya ID yang dimiliki user
        parser.add_argument('POID', type = int, help='You\'re pick a wrong choice of Supplier ID', location='json', choices=tmp_po)
        parser.add_argument('packageID', type = int, help='You\'re pick a wrong choice of Stock ID', location='json',choices=tmp_package)
        parser.add_argument('order', type = int, help='Order quantity', location='json')
        parser.add_argument('unitCost', type = int, help='Order quantity', location='json')
        args = parser.parse_args()

        # get packages name
        qrypackageName = Packages.query.filter_by(id=args['packageID']).first()

        # Get inStock or Beginning Stock
        # Seharusnya yang dijumlah adalah ending dari summary
        qryinStock = Stocks.query.filter_by(packagesID=args['packageID']).all()
        inStock = 0
        for item in qryinStock:
            inStock += item.beginning

        # Perhitungan Sub Total
        subTotal = float(args['order'])*args['unitCost']

        add_po = PODetails(
            POID = args['POID'],
            packageID = args['packageID'],
            packageName = qrypackageName.package_name,
            inStock = inStock,
            order = args['order'],
            unitCost = args['unitCost'],
            subTotal = subTotal
        )
        
        db.session.add(add_po)
        db.session.commit()

        qry = PODetails.query.filter_by(POID=args['POID'],packageID=args['packageID']).first()

        return {
            "message": "Add PO Details Success",
            "PODetails": marshal(qry, podetail_fields)
        } ,200