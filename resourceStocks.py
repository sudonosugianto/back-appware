from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request


from models import db
####### Tempat import Model#########
from modelStocks import Stocks 
from modelPackages import Packages
####### Finish import Model#########

####### Tempat import Field#########
from marshalField import stock_fields
####### Finish import Field#########

class StockResources(Resource):
    # Untuk Post Initiate Stock
    @jwt_required
    def post(self):
        my_identity = get_jwt_identity()
        # qrypackages = Packages.query.filter_by(userPackageID = my_identity).all()

        # Script get the PackageID per User
        # Output File tmp nantinya [1,3, ..etc]
        # tmp = []
        # for item in qrypackages:
        #     tmp.append(item.id)

        parser = reqparse.RequestParser()
        # Package ID diberikan choices hanya ID yang dimiliki user
        parser.add_argument('packagesID', type = int, help='You\'re pick a wrong choice', location='json')
        parser.add_argument('beginning', type = int, help='beginning must be int type', location='json')
        args = parser.parse_args()

        add_stocks = Stocks(
            userStocksID= my_identity,
            packagesID = args['packagesID'],
            beginning = args['beginning']
        )

        qry = Stocks.query.filter_by(packagesID=args['packagesID']).all()
        
        db.session.add(add_stocks)
        db.session.commit()

        return {
            "message": "Add Initiate Stock Success",
            # "package": marshal(qryp,{'id':fields.Integer,\
            #                                 'package_name':fields.String}),
            "stock": marshal(qry, stock_fields)
        } ,200

    @jwt_required
    def put(self,id):
        my_identity = get_jwt_identity()

        qry = Stocks.query.filter_by(userStocksID = my_identity)
        
        if qry == None :
            return {'message': 'stock not found'}, 404

        parser = reqparse.RequestParser()
        # Package ID diberikan choices hanya ID yang dimiliki user
        parser.add_argument('packagesID', type = int, help='packagesID must be integer and exist', location='json')
        parser.add_argument('purchaseOrder', type = int, help='purchaseOrder must be int type', location='json')
        parser.add_argument('sale', type = int, help='sale must be int type', location='json')
        parser.add_argument('adjustment', type = int, help='adjustment must be int type', location='json')

        args = parser.parse_args()

        qry = Stocks.query.filter_by(id=id).first()
        if args['packagesID'] is not None:
            qry.packagesID = args['packagesID']
        if args['purchaseOrder'] is not None:
            qry.purchaseOrder = args['purchaseOrder']
        if args['sale'] is not None:
            qry.sale = args['sale']
        if args['adjustment'] is not None:
            qry.adjustment = args['adjustment']
        
        qry.updated_at = db.func.current_timestamp()

        db.session.add(qry)
        db.session.commit()

        # Perhitungan Ending
        theory = qry.beginning + qry.purchaseOrder - qry.sale
        actualStock = qry.adjustment
        ending = theory - actualStock
        return {
            "message": "Update Stock Success",
            "stock": marshal(qry, stock_fields),
            "ending": ending
        } ,200

     # Untuk menampilkan stocks
    @jwt_required
    def get(self, id=None):
        my_identity = get_jwt_identity()
        
        if id is not None:
            qry = Stocks.query.get(ident=id)
            return {"stocks":marshal(qry, stock_fields)}
        else:
            qry = Stocks.query.filter_by(userStocksID = my_identity).all()
        
        return { "message":"Success",
                 "stocks": marshal(qry, stock_fields)}, 200
