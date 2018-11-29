from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime
from sqlalchemy import or_, func, desc
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
from marshalField import category_fields, item_fields
####### Finish import Marshal#########


class CategorySummaryResources(Resource):
    
    @jwt_required
    def get(self):
        summary = []
        my_identity = get_jwt_identity()
        # Get Category per user
        qryCategory = Category.query.filter_by(userID = my_identity).all()
        
        for i in range(0,len(qryCategory)):
            catID = qryCategory[i].id
            catName = qryCategory[i].category
            
            # query Item Berdasarkan  Kategori
            qryPOperCategory = PO.query.join(Packages, PO.packagePOID == Packages.id)\
                                       .join(Items, Packages.itemID == Items.id)\
                                       .filter(Items.catID == catID).all()
            
            qrySaleperCategory = Sales.query.join(Packages, Sales.packageSalesID == Packages.id)\
                                       .join(Items, Packages.itemID == Items.id)\
                                       .filter(Items.catID == catID).all()

            grossSalePerCategory = 0
            itemSellperCategory = 0
            itemPOPerCategory = 0
            modalPerCategory = 0
            for j in range(0,len(qrySaleperCategory)):
                itemSellperCategory += qrySaleperCategory[j].quantity
                grossSalePerCategory += qrySaleperCategory[j].totalPrice
            
            for i in range(0, len(qryPOperCategory)):
                modalPerCategory += qryPOperCategory[i].totalPrice
                itemPOPerCategory += qryPOperCategory[i].quantity

            Assets = itemPOPerCategory - itemSellperCategory
            meanPriceProduct = grossSalePerCategory / itemSellperCategory
            profitAssets = Assets*meanPriceProduct
            margin = grossSalePerCategory - modalPerCategory
            tmp = {
                    "category": catName,
                    "itemsStock":itemPOPerCategory,
                    "itemsSold": itemSellperCategory,
                    "Assets":Assets,
                    "modalPerCategory":modalPerCategory,
                    "margin":margin,
                    "GSPC": grossSalePerCategory,
                    "MPP": ceil(meanPriceProduct),
                    "profitAssets": ceil(profitAssets)
                    }
            
            summary.append(tmp)
        
        return summary
