
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
from modelSubusers import Subusers

####### Finish import Model#########


####### Tempat import Marshal#########
from marshalField import package_fields
from marshalField import sale_fields
from marshalField import po_fields
from marshalField import actualstock_fields
from marshalField import category_fields
####### Finish import Marshal#########


class SubuserPackagesSummaryResources(Resource):
    def getSoldPackages(self, packageID, selfSales):
        qrySales = selfSales.filter_by(packageSalesID=packageID)
        listQuantity = []
        for item in qrySales.all():
            listQuantity.append(item.quantity)
        totalSoldPackages = sum(listQuantity)
        return totalSoldPackages
    
    def getPOPackages(self, packageID, selfPO):
        qryPO = selfPO.filter_by(packagePOID=packageID)
        listQuantity = []
        for item in qryPO.all():
            listQuantity.append(item.quantity)
        totalPOPackages = sum(listQuantity)
        return totalPOPackages

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

        return stocks

    def get(self):


        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str, location="args", required=True, help="email must be string and exist")
        parser.add_argument("apiKey", type=str, location="args", required=True, help="apiKey must be string and exist")
        args = parser.parse_args()



        qrySubuserByEmail = Subusers.query.filter_by(email=args["email"]).first()
        qrySubuserByAPIkey = Subusers.query.filter_by(apiKey=args["apiKey"]).first()

        if qrySubuserByEmail == qrySubuserByAPIkey:

            my_identity = qrySubuserByAPIkey.userID

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
                packageDetail["packagePO"] = self.getPOPackages(idPackages[i], dataPO)
                packageDetail["assets"] = self.getProfit(idPackages[i], dataPO, dataSales)
                # packageDetail["netSales"] = ceil(self.getTotalSalesPackages(idPackages[i], dataSales))
                # packageDetail["profit"] = ceil(self.getProfit(idPackages[i], dataPO, dataSales))

                listPackageDetail.append(packageDetail)
                packageDetail = {}

            if listPackageDetail == []:
                return {"message": "data not found"}, 404

            return listPackageDetail, 200

        return {"message": "unauthorized"}, 401