from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime
from sqlalchemy import or_, desc

from models import db
####### Tempat import Model#########
from modelPackages import Packages
from modelItems import Items
from modelPO import PO
from modelSales import Sales
from modelPackagesTrack import PackagesTrack
from modelSubusers import Subusers
####### Finish import Model#########


####### Tempat import Marshal#########
from marshalField import packagetrack_fields
from marshalField import item_fields
####### Finish import Marshal#########

class SubuserPackageTrackDetail(Resource):
    def get(self, id = None):
        # Flow mendapatkan track detail Information
        # Filter by user => Filter by package => Filter_by PO
        
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str, location="args", required=True, help="email must be string and exist")
        parser.add_argument("apiKey", type=str, location="args", required=True, help="apiKey must be string and exist")
        parser.add_argument('code', type = str, help='code must be Integer', location ='args',required=True)
        args = parser.parse_args()

        # Query untuk melihat subuser
        qrySubuserByEmail = Subusers.query.filter_by(email=args["email"]).first()
        qrySubuserByAPIkey = Subusers.query.filter_by(apiKey=args["apiKey"]).first()


        if qrySubuserByEmail == qrySubuserByAPIkey:
            my_identity = qrySubuserByAPIkey.userID
            
            
            qry = PackagesTrack.query.join(PO, PO.id == PackagesTrack.POID)\
                                    .filter(PO.userPOID == my_identity)\
                                    .filter(PackagesTrack.code == args['code']).first()
            
            if qry is None:
                return {"message":"Items / Package not Found or maybe it has been sold"} , 404

            # Status True artinya belum terjual / masih di gudang
            # Status False artinya sudah terjual
            if qry.status == True:
                detailPackageField = {
                    "code": fields.String,
                    "packages.Items.item":fields.String,
                    "packages.package_name": fields.String,
                    "po.id":fields.String,
                    "po.suppliers.name":fields.String,
                    "po.quantity":fields.String,
                    # "sales.id":fields.Integer,
                    # "sales.customers.fullname":fields.String,
                    # "sales.quantity":fields.String,
                    "created_at":fields.DateTime(dt_format='rfc822'),
                    "updated_at":fields.DateTime(dt_format='rfc822')
                }
                return  marshal(qry, detailPackageField),200
            
            elif qry.status == False:
                detailPackageField = {
                    "code": fields.String,
                    "packages.Items.item":fields.String,
                    "packages.package_name": fields.String,
                    "po.id":fields.Integer,
                    "po.suppliers.name":fields.String,
                    "po.quantity":fields.String,
                    "sales.id":fields.Integer,
                    "sales.customers.fullname":fields.String,
                    "sales.quantity":fields.String,
                    "created_at":fields.DateTime(dt_format='rfc822'),
                    "updated_at":fields.DateTime(dt_format='rfc822')
                }

                return  marshal(qry, detailPackageField), 200

        return {"message": "unauthorized"}, 401


