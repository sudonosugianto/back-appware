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
        
        parser = reqparse.RequestParser()
        parser.add_argument("dateStart", type=str, location="args", help="Date Time must be in format YYYY-MM-DD HH:MM:SS")
        parser.add_argument("dateEnd", type=str, location="args", help="Date Time must be in format YYYY-MM-DD HH:MM:SS")
        parser.add_argument("search", type=str, location="args", help="search must string")
        args = parser.parse_args()

        # dateInput = datetime.strptime(args['date'], '%Y-%m-%d %H:%M:%S')

        dateStart = args['dateStart']
        dateEnd = args['dateEnd']
        
        qryPackage = Packages.query.join(Items, Packages.itemID == Items.id)\
                                   .filter(Packages.userPackageID == my_identity)
        qryPO = PO.query.join(Packages, PO.packagePOID == Packages.id).filter(PO.userPOID == my_identity)
        qrySales= Sales.query.join(Packages, Sales.packageSalesID == Packages.id).filter(Sales.userSalesID == my_identity)
        qryActualStock = ActualStock.query.filter(ActualStock.userActualStocksID == my_identity)

        # Filter by date
        if args['dateStart'] != None and args['dateEnd'] != None:
            qryPO = qryPO.filter(and_(PO.created_at >= dateStart, PO.created_at <= dateEnd))
            qrySales = qrySales.filter(and_(Sales.created_at >= dateStart, Sales.created_at <= dateEnd))

        # Fitur untuk Search
        if args['search'] is not None:
            search = args['search']
            qryPackage = qryPackage.filter(or_(Packages.package_name.like("%"+search+"%"),\
                                               Items.item.like("%"+search+"%"))).all()
        else:
            qryPackage = qryPackage.all()
        
        for i in range(0,len(qryPackage)):
            packageID = qryPackage[i].id
            itemName = qryPackage[i].Items.item + ' per ' + qryPackage[i].package_name
            catName = qryPackage[i].Category.category
 
            
            qry = qryPO.filter(Packages.id == packageID).all()
            qrySale = qrySales.filter(Packages.id == packageID).all()
            qryActual = qryActualStock.filter(ActualStock.packageActualStocksID == packageID)\
                                      .order_by(desc(ActualStock.created_at)).first()

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
            if qryActual is not None:
                totalActual = qryActual.actual_stock
            else:
                totalActual = totalPO - totalSales
            #########  End of Perhitungan Actual Stock per Packages #########
            
            teori = totalPO - totalSales
            adjusment = totalActual - teori


            tmp = { "message":"Summary per Item Package", 
                "Package": itemName,
                "Category": catName,
                "POQuantity": totalPO,
                "salesQuantity": totalSales,
                "stock": teori,
                "adjusment": adjusment,
                "actualStock": totalActual
                }
            summary.append(tmp) 
            
        return summary