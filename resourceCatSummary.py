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
        TopItemCatAll = []
        my_identity = get_jwt_identity()
        # Get Category per user
        qryCategory = Category.query.filter_by(userID = my_identity).all()
        
        for i in range(0,len(qryCategory)):
            catID = qryCategory[i].id
            catName = qryCategory[i].category

            TopItemAll = []
            tmp = { catName : TopItemAll}
            
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
            allProductPrice = 0
            for j in range(0,len(qrySaleperCategory)):
                itemSellperCategory += qrySaleperCategory[j].quantity
                grossSalePerCategory += qrySaleperCategory[j].totalPrice
            
            for i in range(0, len(qryPOperCategory)):
                allProductPrice += qryPOperCategory[i].totalPrice
                itemPOPerCategory += qryPOperCategory[i].quantity

            Assets = itemPOPerCategory - itemSellperCategory
            meanPriceProduct = grossSalePerCategory / itemSellperCategory
            profitAssets = Assets*meanPriceProduct
            return({
                    # "PO":marshal(qryPOperCategory, po_fields),
                    # "Sales":marshal(qrySaleperCategory, sale_fields),
                    "items Stock":itemPOPerCategory,
                    "items Sold": itemSellperCategory,
                    "Assets":Assets,
                    "Harga Beli Semua Produk":allProductPrice,
                    "GSPC": grossSalePerCategory,
                    "MPP": ceil(meanPriceProduct),
                    "profitAssets": ceil(profitAssets)})

        #         itemID = qryPOperCategory[j].id
        #         itemName = qryPOperCategory[j].item
                
        #         # query Packages Berdasarkan Item
        #         qryItemsPack = Packages.query.filter_by(itemID = itemID).first()
                
        #         packageID = qryItemsPack.id
        #         packageName = qryItemsPack.package_name

        #         # Start Perhitungan Jumlah Sales per Package #############
        #         qrySale = Sales.query.filter_by(userSalesID = my_identity)\
        #                             .filter_by(packageSalesID = packageID).all()
        #         jumlahSaleperPackage = 0
        #         for k in range(0,len(qrySale)):
        #             jumlahSaleperPackage += qrySale[k].quantity
        #         # End of Perhitungan Jumlah Sales per Package #############

        #         TopItemAll.append({"itemID":itemID,"name":itemName,\
        #                             "packageID":packageID,"packageName":packageName,
        #                             "totalItem":jumlahSaleperPackage})
        #     TopItemCatAll.append(tmp)

        # # print(TopItemAll)
        # return {"result":TopItemCatAll}