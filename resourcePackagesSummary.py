
from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime
from sqlalchemy import or_, func, desc, and_
from datetime import datetime, timedelta
from math import ceil

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
        for item in qrySales.all():
            listQuantity.append(item.quantity)
        totalSoldPackages = sum(listQuantity)
        return totalSoldPackages
    
    def getTotalSalesPackages(self, packageID, selfSales):
        qrySales = selfSales.filter_by(packageSalesID=packageID)
        listTotalPrice = []
        for item in qrySales.all():
            listTotalPrice.append(item.totalPrice)
        totalPrice = sum(listTotalPrice)
        return totalPrice

    def getProfit(self, packageID, selfPO, selfSales):

        qryPO = selfPO.filter_by(packagePOID=packageID)
        listTotalPO = []
        listQuantityPO = []
        for item in qryPO.all():
            listTotalPO.append(item.totalPrice)
            listQuantityPO.append(item.quantity)
        totalPO = sum(listTotalPO)
        quantityPO= sum(listQuantityPO)

        qrySales = selfSales.filter_by(packageSalesID=packageID)
        listTotalSales = []
        listQuantitySales = []
        for item in qrySales.all():
            listTotalSales.append(item.totalPrice)
            listQuantitySales.append(item.quantity)
        totalSales = sum(listTotalSales)
        quantitySales = sum(listQuantitySales)

        if totalSales == 0 or quantitySales == 0:
            meanSalesPrice = 0
        else:
            meanSalesPrice = totalSales / quantitySales

        stocks = quantityPO - quantitySales

        profit = totalSales - totalPO + meanSalesPrice * stocks

        return profit

    @jwt_required
    def get(self):
        my_identity = get_jwt_identity()
        dataPackages = Packages.query.filter_by(userPackageID=my_identity).order_by(Packages.package_name)
        dataSales = Sales.query.filter_by(userSalesID=my_identity)
        dataPO = PO.query.filter_by(userPOID=my_identity)
        idPackages = []
        namePackages = []
        for item in dataPackages.all():
            idPackages.append(item.id)
            namePackages.append(item.package_name)
        listPackageDetail = []
        packageDetail = {}
        for i in range (0, len(idPackages)):
            packageDetail["packageID"] = idPackages[i]
            packageDetail["packageName"] = namePackages[i]
            qry = Packages.query.filter_by(id = idPackages[i]).first()
            catID = qry.catPackageID
            itemID = qry.itemID
            packageDetail["itemName"] = Items.query.filter_by(id = itemID).first().item
            packageDetail["categoryName"] = Category.query.filter_by(id = catID).first().category
            packageDetail["packageSold"] = self.getSoldPackages(idPackages[i], dataSales)
            packageDetail["netSales"] = ceil(self.getTotalSalesPackages(idPackages[i], dataSales))
            packageDetail["profit"] = ceil(self.getProfit(idPackages[i], dataPO, dataSales))
            # packageDetail["packagePO"] = self.getProfit(idPackages[i], dataPO, dataSales)[2]

            listPackageDetail.append(packageDetail)
            packageDetail = {}


        return listPackageDetail, 200