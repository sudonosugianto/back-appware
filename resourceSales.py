from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime
from sqlalchemy import desc


from models import db


####### Tempat import Model#########
from modelSales import Sales
####### Finish import Model#########


####### Tempat import Marshal#########
from marshalField import sale_fields
####### Finish import Marshal#########


class SaleResources(Resource):

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
        
        # qry untuk mendapatkan post PO terakhir oleh user
        qry = Sales.query.filter_by(userSalesID=my_identity).order_by(desc(Sales.created_at)).first()

        return {
            "message": "add sale success",
            "customer": marshal(add_sale, sale_fields)
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

        qry = Sales.query

        #   get by id

        if id != None:
            qry = qry.filter_by(userSalesID = my_identity).filter_by(id = id)

            rows = []

            for row in qry.all():
                rows.append(marshal(row, sale_fields))

            if rows == []:
                return {'message': 'sale not found'}, 404

            return {
                "message": "success",
                "sale": rows
            }, 200

        # get all
        qry = qry.filter_by(userSalesID=my_identity)
        rows = []

        for row in qry.all():
            rows.append(marshal(row, sale_fields))

        if rows == []:
            return {'message': 'sale not found'}, 404

        return {
            "message": "success",
            "sales": rows
        }, 200