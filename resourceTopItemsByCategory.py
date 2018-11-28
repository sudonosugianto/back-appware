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
from marshalField import category_fields, item_fields
####### Finish import Marshal#########


class TopItemsByCatResources(Resource):
    
    @jwt_required
    def get(self):
        TopItemCatAll = []
        my_identity = get_jwt_identity()
        # Get Category per user
        qryCategory = Category.query.filter_by(userID = my_identity).all()
        qryPackage = Packages.query.filter_by(userPackageID = my_identity).all()

        TopItemAll = []
        for i in range(0,len(qryCategory)):
            catID = qryCategory[i].id
            catName = qryCategory[i].category

            
            
            # query Item Berdasarkan  Kategori
            qryItems = Items.query.filter_by( userID = my_identity).filter_by(catID = catID).all()
            
            for j in range(0,len(qryItems)):
                itemID = qryItems[j].id
                itemName = qryItems[j].item
                
                # query Item Package Berdasarkan  Kategori
                qryItemsPack = Packages.query.filter_by(itemID = itemID).first()
                
                packageID = qryItemsPack.id
                packageName = qryItemsPack.package_name

                # Start Perhitungan Jumlah Sales per Package #############
                qrySale = Sales.query.filter_by(userSalesID = my_identity)\
                                    .filter_by(packageSalesID = packageID).all()
                jumlahSaleperPackage = 0
                for k in range(0,len(qrySale)):
                    jumlahSaleperPackage += qrySale[k].quantity
                # End of Perhitungan Jumlah Sales per Package #############

                TopItemAll.append({"category":catName,"itemID":itemID,"name":itemName,\
                                    "packageID":packageID,"packageName":packageName,
                                    "totalItem":jumlahSaleperPackage})
            

        # print(TopItemAll)
        return TopItemAll