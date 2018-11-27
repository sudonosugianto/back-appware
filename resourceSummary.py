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
####### Finish import Model#########


####### Tempat import Marshal#########
from marshalField import package_fields
from marshalField import sale_fields
from marshalField import po_fields, actualstock_fields
####### Finish import Marshal#########


class SummaryResources(Resource):

    def getQuantityPOPerDay(self, packageID, selfPO):
        # filter per hari
        filter_day = datetime.today()
        qryPO = selfPO.filter(PO.created_at <= filter_day)
        # filter per package
        qryPO = qryPO.filter_by(packagePOID=packageID).all()
        # dapatkan quantity PO per hari
        items = []
        for item in qryPO:
            items.append(item.quantity)       
        POPerDay = sum(items)
        return POPerDay

    def getQuantitySalePerDay(self, packageID, selfSale):
        # filter per hari
        filter_day = datetime.today()
        qrySale = selfSale.filter(Sales.created_at <= filter_day)
        # filter per package
        qrySale = qrySale.filter_by(packageSalesID=packageID).all()
        # dapatkan quantity sales per hari
        items = []
        for item in qrySale:
            items.append(item.quantity)
        SalesPerDay = sum(items)
        return SalesPerDay

    def getActualStock(self, packageID, selfActualStock):
        filter_day = datetime.today()
        qryActualStock = selfActualStock.filter_by(packageActualStocksID=packageID).first()
        
        if qryActualStock == None:
            qryActualStock = "kosong"
            return qryActualStock
        
        actual_stock = marshal(qryActualStock, actualstock_fields)["actual_stock"]
        return actual_stock

    # Untuk menampilkan summary
    @jwt_required
    def get(self):

        my_identity = get_jwt_identity()


        dataPackages = Packages.query.filter_by(userPackageID=my_identity).all()
        dataPO = PO.query.filter_by(userPOID=my_identity)
        dataSales = Sales.query.filter_by(userSalesID=my_identity)
        dataActualStock = ActualStock.query.filter_by(userActualStocksID=my_identity)

        rows = []
        for row in dataPackages:
            rows.append(marshal(row, package_fields))

        
        idPackages = []
        namePackages = []
        for item in rows:
            idPackages.append(item['id'])
            namePackages.append(item['package_name'])
        
        packageDetail = {}
        result= []
        
        for i in range (0, len(idPackages)):
            # filter_day = datetime.today
            packageName = namePackages[i]
            showPO = self.getQuantityPOPerDay(idPackages[i], dataPO)
            showSale = self.getQuantitySalePerDay(idPackages[i], dataSales)
            showActualStock = self.getActualStock(idPackages[i], dataActualStock)
            packageDetail["date"] = "today"
            packageDetail["packageName"] = packageName
            packageDetail["PO"] = showPO
            packageDetail["sales"] = showSale
            teori = showPO - showSale

            if showActualStock == "kosong":
                showActualStock = teori

            packageDetail["actualStock"] = showActualStock
            packageDetail["adjustment"] = showPO - showSale - showActualStock
            packageDetail["Ending"] = showPO - showSale - (showPO - showSale - showActualStock)
            result.append(packageDetail)
            packageDetail = {}

        return {"result": result}, 200