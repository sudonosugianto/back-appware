from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime
from sqlalchemy import or_, func, desc, and_
from datetime import datetime, timedelta

from models import db
####### Tempat import Model#########
from modelPackages import Packages
from modelItems import Items
from modelPO import PO
from modelSales import Sales
from modelActualStock import ActualStock
from modelCat import Category

####### Finish import Model#########


####### Tempat import Marshal#########
from marshalField import package_fields
from marshalField import sale_fields
from marshalField import po_fields
from marshalField import actualstock_fields
from marshalField import category_fields
####### Finish import Marshal#########

class POSalesTransactionResources(Resource):
    @jwt_required
    def get(self):
        self_po_fields = {
            # "id": fields.Integer,
            "suppliers.name": fields.String,
            "packages.package_name": fields.String,
            "packages.Items.item": fields.String,
            "quantity": fields.Integer,
            "buyingPricePerPackage": fields.Float,
            "totalPrice": fields.Float,
            "created_at": fields.String
        }
        self_sale_fields = {
            # "id": fields.Integer,
            "customers.fullname": fields.String,
            "packages.package_name": fields.String,
            "packages.Items.item": fields.String,
            "quantity": fields.Integer,
            "sellingPricePerPackage": fields.Float,
            "totalPrice":fields.Float,
            "created_at": fields.String
        }

        my_identity = get_jwt_identity()

        parser = reqparse.RequestParser()
        parser.add_argument("dateStart", type=str, location="args", help="Date Time must be in format YYYY-MM-DD HH:MM:SS")
        parser.add_argument("dateEnd", type=str, location="args", help="Date Time must be in format YYYY-MM-DD HH:MM:SS")
        args = parser.parse_args()

        dateStart = args['dateStart']
        dateEnd = args['dateEnd']

        qryPO = PO.query.filter(PO.userPOID==my_identity)
        qrySales = Sales.query.filter_by(userSalesID=my_identity)

         # Filter by date
        if args['dateStart'] != None and args['dateEnd'] != None:
            qryPO = qryPO.filter(and_(PO.created_at >= dateStart, PO.created_at <= dateEnd)).order_by(desc(PO.created_at))
            qrySales = qrySales.filter(and_(Sales.created_at >= dateStart, Sales.created_at <= dateEnd)).order_by(desc(Sales.created_at))

        listDataPO = []

        for item in qryPO.all():
            listDataPO.append(marshal(item, self_po_fields))

        listDataSales = []

        for item in qrySales.all():
            listDataSales.append(marshal(item, self_sale_fields))


        return {
            "dateStart": dateStart,
            "dateEnd": dateEnd,
            "dataPO": listDataPO,
            "dataSales": listDataSales
        }, 200