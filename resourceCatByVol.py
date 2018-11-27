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


class CatByVolResources(Resource):

    def getQuantityPO(self, packageID, selfPO):
        # filter per package
        qryPO = selfPO.filter_by(packagePOID=packageID).all()
        # dapatkan quantity PO total
        items = []
        for item in qryPO:
            items.append(item.quantity)       
        TotalPO = sum(items)
        print('total po', TotalPO)
        return TotalPO

    def getQuantitySale(self, packageID, selfSale):
        # filter per package
        qrySale = selfSale.filter_by(packageSalesID=packageID).all()
        # dapatkan quantity sales
        items = []
        for item in qrySale:
            items.append(item.quantity)
        TotalSales = sum(items)
        return TotalSales

    @jwt_required
    def get(self):
        my_identity = get_jwt_identity()
        dataPO = PO.query.filter_by(userPOID=my_identity)
        dataSales = Sales.query.filter_by(userSalesID=my_identity)

        dataCategories = Category.query.filter_by(userID=my_identity)
        listCategories = []
        for item in dataCategories:
            listCategories.append(marshal(item, category_fields))
        idCategories = []
        nameCategories = []
        for item in listCategories:
            idCategories.append(item["id"])
            nameCategories.append(item["category"]) 

        dataPackages = Packages.query.filter_by(userPackageID=my_identity)

        listA = []
        listPackages = []
        idPackages = []

        for item in idCategories:
            data = dataPackages.filter_by(catPackageID=item).all()
            for item in data:
                listPackages.append(marshal(item, package_fields))

            for pckg in listPackages:
                idPackages.append(pckg["id"])
                
            listA.append(idPackages)
            listPackages = []
            idPackages = []
        # return listA

        showPO = 0
        showSale =  0

        for item1 in listA:
            for item2 in item1:
                showPO += self.getQuantityPO(item2, dataPO)
                showSale += self.getQuantitySale(item2, dataSales)
                
        return {
            "PO": showPO,
            "Sales": showSale
        }, 200