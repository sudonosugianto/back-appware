from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request


from models import db
####### Tempat import Model#########
from modelStocks import Stocks 
from modelPackages import Packages
####### Finish import Model#########

####### Tempat import Field#########
from marshalField import package_fields
####### Finish import Field#########

class StockResources(Resource):
    # Untuk Post Initiate Stock
    @jwt_required
    def post(self):
        my_identity = get_jwt_identity()
        qrypackages = Packages.query.filter_by(userPackageID = my_identity).all()

        # Script get the PackageID per User
        # Output File tmp nantinya [1,3, ..etc]
        tmp = []
        for item in qrypackages:
            tmp.append(item.id)

        parser = reqparse.RequestParser()
        # Package ID diberikan choices hanya ID yang dimiliki user
        parser.add_argument('packagesID', type = int, help='You\'re pick a wrong choice', location='json', choices=tmp)
        parser.add_argument('beginning', type = int, help='beginning must be int type', location='json')
        args = parser.parse_args()

        add_stocks = Stocks(
            packagesID = args['packagesID'],
            beginning = args['beginning']
        )

        qry = Stocks.query.filter_by(packagesID=args['packagesID']).all()
        
        db.session.add(add_stocks)
        db.session.commit()

        return {
            "message": "Add Initiate Stock Success",
            "package": marshal(qrypackages,{'id':fields.Integer,\
                                            'package_name':fields.String}),
            "stock": marshal(qry, package_fields)
        } ,200

    @jwt_required
    def put(self,id=None):
        my_identity = get_jwt_identity()
        qrypackages = Packages.query.filter_by(userPackageID = my_identity).all()

        # Script get the PackageID per User
        # Output File tmp nantinya [1,3, ..etc]
        tmp = []
        for item in qrypackages:
            tmp.append(item.id)

        parser = reqparse.RequestParser()
        # Package ID diberikan choices hanya ID yang dimiliki user
        parser.add_argument('packagesID', type = int, help='You\'re pick a wrong choice', location='json', choices=tmp)
        parser.add_argument('beginning', type = int, help='beginning must be int type', location='json')
        args = parser.parse_args()

        qry = Stocks.query.filter_by(id=id).first()
        if args['packagesID'] is not None:
            qry.packagesID = args['packagesID']
        if args['beginning'] is not None:
            qry.beginning = args['beginning']
        
        qry.updated_at = db.func.current_timestamp()
        db.session.add(qry)
        db.session.commit()

        return {
            "message": "Update Initiate Stock Success",
            "package": marshal(qrypackages,{'id':fields.Integer,\
                                            'package_name':fields.String}),
            "stock": marshal(qry, package_fields)
        } ,200