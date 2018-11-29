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
    # Untuk menampilkan summary
    @jwt_required
    def get(self):
        summary=[]
        my_identity = get_jwt_identity()
        
        qryPackage = Packages.query.filter_by(userPackageID = my_identity).all()

        qryPO = PO.query.join(Packages, PO.packagePOID == Packages.id).filter(PO.userPOID == my_identity)
        qrySales= Sales.query.join(Packages, Sales.packageSalesID == Packages.id).filter(Sales.userSalesID == my_identity)
        qryActualStock = ActualStock.query.filter(ActualStock.userActualStocksID == my_identity)

        for i in range(0,len(qryPackage)):
            packageID = qryPackage[i].id
            itemName = qryPackage[i].Items.item + ' ' + qryPackage[i].package_name
 
            
            qry = qryPO.filter(Packages.id == packageID).all()
            qrySale = qrySales.filter(Packages.id == packageID).all()
            qryActual = qryActualStock.filter(ActualStock.packageActualStocksID == packageID).all()

            #########  Start Perhitungan Total PO per Packages #########
            totalPO = 0
            for j in range(0,len(qry)):
                totalPO += qry[j].quantity
            #########  End of Perhitungan Total PO per Packages #########
            #########  Start Perhitungan Total PO per Packages #########
            totalSales = 0
            for j in range(0,len(qrySale)):
                totalSales += qrySale[j].quantity
            #########  End of Perhitungan Total PO per Packages #########
            
            #########  Start Perhitungan Actual Stock per Packages #########
            if qryActual != []:
                totalActual = 0
                for j in range(0,len(qryActual)):
                    totalActual += qryActual[j].actual_stock
            else:
                totalActual = totalPO - totalSales
            #########  End of Perhitungan Actual Stock per Packages #########
            
            Ending = totalPO - totalSales
            Adjusment = Ending - totalActual
            
            tmp = { "message":"Summary per Item Package", 
                "Package": itemName,
                "POQuantity": totalPO,
                "SalesQuantity": totalSales,
                "Adjusment": Adjusment,
                # "ActualStock": totalActual,
                "Ending":Ending}

            summary.append(tmp) 
            
        
        return summary
