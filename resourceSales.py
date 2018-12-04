from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime
from sqlalchemy import desc, and_, or_


from models import db


####### Tempat import Model#########
from modelSales import Sales
from modelCat import Category
from modelPackages import Packages
from modelPackagesTrack import PackagesTrack
from modelItems import Items
####### Finish import Model#########


####### Tempat import Marshal#########
from marshalField import sale_fields
from marshalField import packagetrack_fields
####### Finish import Marshal#########


class SaleResources(Resource):
    @jwt_required
    def Out(self,packageID,saleID,saleQty):
        my_identity = get_jwt_identity()
        qryGoSale = PackagesTrack.query.join(Packages, PackagesTrack.packageID == Packages.id)\
                             .filter(Packages.userPackageID == my_identity)\
                             .filter(PackagesTrack.packageID == packageID)\
                             .filter(PackagesTrack.status == True).all()

        # Generate Barang yang akan keluar 
        listTrack = []
        for i in range(0,saleQty):
            qryGoSale[i].salesID = saleID
            qryGoSale[i].status = False
            # changeStatus = list(qryGoSale[i].code)
            # changeStatus[-1:] ="F"
            # qryGoSale[i].code = "".join(changeStatus)
            qryGoSale[i].updated_at = db.func.current_timestamp()
            db.session.commit()
            listTrack.append(qryGoSale[i].code)
        return listTrack

    # Untuk tambah Sale
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("customerSalesID", type=int, location="json", required=True, help="customerSalesID must be integer and exist")
        parser.add_argument("packageSalesID", type=int, location="json", required=True, help="packageSalesID must be integer and exist")
        parser.add_argument("quantity", type=int, location="json", required=True, help="quantity must be integer and exist")
        parser.add_argument("sellingPricePerPackage", type=float, location="json", required=True, help="sellingPrice must be float and exist")
        args = parser.parse_args()
        my_identity = get_jwt_identity()
        
        ############### Start of Check Maksimal Sales ################################
        qryGoSale = PackagesTrack.query.join(Packages, PackagesTrack.packageID == Packages.id)\
                             .filter(Packages.userPackageID == my_identity)\
                             .filter(PackagesTrack.packageID == args['packageSalesID'])\
                             .filter(PackagesTrack.status == True).all()
        totalItem = len(qryGoSale)
        print(totalItem)
        # return {"message":totalItem,
        #         "Item sah":marshal(qryGoSale, packagetrack_fields)}
        if args['quantity'] >  totalItem:
            return {"message":"You can't Sale Item more than of your Stock"}
        
        ################# End of Check Maksimal Sales ####################################
        
        # Total Sale
        totalPrice = float(args['quantity'])*args['sellingPricePerPackage']

        add_sale = Sales(
            userSalesID = my_identity,
            customerSalesID = args['customerSalesID'],
            packageSalesID= args['packageSalesID'],
            quantity= args['quantity'],
            sellingPricePerPackage = args['sellingPricePerPackage'],
            totalPrice =totalPrice
        )

        db.session.add(add_sale)
        db.session.commit()
        
        # qry untuk mendapatkan post Sales terakhir oleh user
        qry = Sales.query.filter_by(userSalesID=my_identity).order_by(desc(Sales.created_at)).first()

        listTrack = self.Out(args['packageSalesID'],qry.id,args['quantity'])
        # 
        return {
            "message": "add sale success",
            "IdKeluar": listTrack,
            "customer": marshal(add_sale, sale_fields),
            "sales": marshal(qry, sale_fields)
        }, 200

    # untuk edit sale
    @jwt_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("customerSalesID", type=int, location="json", required=True, help="customerSalesID must be integer and exist")
        parser.add_argument("packageSalesID", type=int, location="json", required=True, help="packageSalesID must be integer and exist")
        parser.add_argument("quantity", type=int, location="json", required=True, help="quantity must be integer and exist")
        parser.add_argument("sellingPricePerPackage", type=float, location="json", required=True, help="sellingPrice must be float and exist")
        args = parser.parse_args()

        my_identity = get_jwt_identity()

        qry = Sales.query.filter_by(userSalesID = my_identity).filter_by(id = id).first()

        if qry == None :
            return {'message': 'Sale not found'}, 404

        else:
            if args["customerSalesID"] != None:
                qry.customerSalesID= args["customerSalesID"]
            if args["packageSalesID"] != None:
                qry.packageSalesID= args["packageSalesID"]
            if args["quantity"] != None:
                qry.quantity= args["quantity"]
            if args["sellingPricePerPackage"] != None:
                qry.sellingPricePerPackage= args["sellingPricePerPackage"]

            qry.updated_at = db.func.current_timestamp()

            db.session.add(qry)
            db.session.commit()

            return {
                "message": "edit sale success",
                "sale": marshal(qry, sale_fields)
            } ,200

    @jwt_required
    def delete(self, id):
        my_identity = get_jwt_identity()
        qry = Sales.query.filter_by(userSalesID = my_identity).filter_by(id = id).first()
        if qry == None:
            return {'message': "sale not found!"}, 404

        db.session.delete(qry)
        db.session.commit()

        return {'message': "delete sale success"}, 200

    # Menampilkan sales
    @jwt_required
    def get(self, id=None):

        my_identity = get_jwt_identity()

        parser = reqparse.RequestParser()
        parser.add_argument("search", type=str, location="args", help="search must string")
        parser.add_argument('sort',location='args',help='invalid sort',choices=('desc','asc'))
        parser.add_argument("dateStart", type=str, location="args", help="Date Time must be in format YYYY-MM-DD HH:MM:SS")
        parser.add_argument("dateEnd", type=str, location="args", help="Date Time must be in format YYYY-MM-DD HH:MM:SS")
        args = parser.parse_args()

        # dateStart = datetime.strptime(args['dateStart'], '%Y-%m-%d %H:%M:%S')
        # dateEnd = datetime.strptime(args['dateEnd'], '%Y-%m-%d %H:%M:%S')
        dateStart = args['dateStart']
        dateEnd = args['dateEnd']

        qry = Sales.query.join(Packages, Sales.packageSalesID == Packages.id)\
                         .join(Items, Packages.itemID == Items.id)\
                         .join(Category, Category.id == Packages.catPackageID)\
                         .filter(Sales.userSalesID == my_identity)

        # Filter by date
        if args['dateStart'] != None and args['dateEnd'] != None:
            qry = qry.filter(and_(Sales.created_at >= dateStart, Sales.created_at <= dateEnd))

        rows = []
        #   Get by ID
        if id != None:
            qry = qry.filter(Sales.id == id)

            for row in qry.all():
                rows.append(marshal(row, sale_fields))

            if rows == []:
                return {'message': 'Sales not found'}, 404

            return {
                "message": "success",
                "category.category":fields.String,
                "items.item":fields.String,
                "sales": rows
            }, 200

        else:

            if args['search'] is not None:
                search = args['search']
                # Fungsi untuk search, digunakan filter daripada filter_by 
                # karena butuh method like dengan regex %
                qry = qry.filter(or_(Category.category.like('%'+search+'%'),\
                                     Items.item.like('%'+search+'%')))
            
            if args['sort'] is not None:
                sort = args['sort']
                if sort == "asc":
                    qry = qry.order_by(Sales.created_at)
                elif sort == "desc":
                    qry = qry.order_by(desc(Sales.created_at))

            # get all
            # Semua item deafult nya order secara desc
            qry = qry.order_by(desc(Sales.created_at)).all()

            # Info Format
           
            for row in (qry):
                rows.append(marshal(row, sale_fields))

            if rows == []:
                return {'message': 'sale not found'}, 404

            return {
                "message": "success",
                "sales": rows
            }, 200