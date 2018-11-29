from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime
from sqlalchemy import or_, func, desc
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
        my_identity = get_jwt_identity()
        filter_day = datetime.today()
        dataPO = PO.query\
                            .filter(PO.created_at <= filter_day)\
                            .filter_by(userPOID=my_identity)\
                            .join(Packages, Packages.id == PO.packagePOID)\
                            .order_by(desc(PO.created_at))
        dataSales = Sales.query\
                            .filter(Sales.created_at <= filter_day)\
                            .filter_by(userSalesID=my_identity)\
                            .join(Packages, Packages.id == Sales.packageSalesID)\
                            .order_by(desc(Sales.created_at))
        
        listDataPO = []
        dictDataPO = {}
        for item in dataPO.all():
            dictDataPO["datetime"] = item.created_at
            dictDataPO["packageName"] = Packages.package_name

            listDataPO.append(dictDataPO)
            dictDataPO = {}

        listDataSales = []
        for item in dataSales.all():
            listDataSales.append(marshal(item, sale_fields))
        return {
            "dataPO": listDataPO,
            "dataSales": listDataSales
        }, 200