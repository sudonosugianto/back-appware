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


class PackagesSummaryResources(Resource):
    def getSoldPackages(self, packageID, selfSales):
        qrySales = selfSales.filter_by(packageSalesID=packageID)
        listQuantity = []
        # for item in qrySales:
        #     listQuantity.append(item.)
        pass

    @jwt_required
    def get(self):
        my_identity = get_jwt_identity()
        dataPackages = Packages.query.filter_by(userPackageID=my_identity)
        dataSales = Sales.query.filter_by(userSalesID=my_identity)
        idPackages = []
        namePackages = []
        for item in dataPackages.all():
            idPackages.append(item.id)
            namePackages.append(item.package_name)
        # for i in range (0, len(idPackages)):


        # return namePackages
        pass