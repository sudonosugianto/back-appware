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

class PackageTrackDetail(Resource):
    @jwt_required
    def get(self, id = None):
        # Flow mendapatkan track detail Information
        # Filter by user => Filter by package => Filter_by PO
        my_identity = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument('code', type = str, help='code must be Integer', location ='args')
        args = parser.parse_args()

        detailPackageField = {
                "id":fields.Integer,
                "code": fields.String,
                "packages.Items.id":fields.Integer,
                "packages.Items.item":fields.String,
                "packages.id": fields.Integer,
                "packages.package_name": fields.String,
                "packages.items_quantity": fields.Integer,
                "po.id":fields.Integer,
                "po.suppliers.name":fields.String,
                "po.suppliers.address":fields.String,
                "po.quantity":fields.String,
                "sales.id":fields.Integer,
                "sales.customers.fullname":fields.String,
                "sales.customers.address":fields.String,
                "sales.quantity":fields.String,
                "created_at":fields.DateTime(dt_format='rfc822'),
                "updated_at":fields.DateTime(dt_format='rfc822')
            }
        
        
        if id is not None:
            qry = PackagesTrack.query.filter_by(id = id).first()
            
            if qry is None:
                return {"message":"ID track is not Fpund"} , 404
            return  marshal(qry, detailPackageField),200
        
        if args['code'] is not None:
            qry = PackagesTrack.query.join(PO, PO.id == PackagesTrack.POID)\
                                .filter(PO.userPOID == my_identity)\
                                .filter(PackagesTrack.code == args['code']).first()

            if qry is None:
                return {"message":"Items / Package not Found"} , 404

            # Status True artinya belum terjual / masih di gudang
            # Status False artinya sudah terjual
            if qry.status == True:
                detailPackageField = {
                    "id":fields.Integer,
                    "code": fields.String,
                    "packages.Items.id":fields.Integer,
                    "packages.Items.item":fields.String,
                    "packages.id": fields.Integer,
                    "packages.package_name": fields.String,
                    "packages.items_quantity": fields.Integer,
                    "po.id":fields.Integer,
                    "po.suppliers.name":fields.String,
                    "po.suppliers.address":fields.String,
                    "po.quantity":fields.String,
                    # "sales.id":fields.Integer,
                    # "sales.customers.fullname":fields.String,
                    # "sales.quantity":fields.String,
                    "created_at":fields.DateTime(dt_format='rfc822'),
                    "updated_at":fields.DateTime(dt_format='rfc822')
                }
                return  marshal(qry, detailPackageField),200
            
            elif qry.status == False:

                return  marshal(qry, detailPackageField), 200
            
        else:
            qry = PackagesTrack.query.join(PO, PO.id == PackagesTrack.POID)\
                                        .filter(PO.userPOID == my_identity)\
                                        .order_by(desc(PackagesTrack.id))\
                                        .all()
            
            # Looping untuk mendapatkan semua Transaksi Barang yang Masuk
            rows = []
            for item in qry:
                if item.status == True:
                    rows.append(item)
            
            return marshal(rows, detailPackageField)




