from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime
from sqlalchemy import or_

from models import db
####### Tempat import Model#########
from modelActuaStock import ActualStock
####### Finish import Model#########


####### Tempat import Marshal#########
from marshalField import actualstock_fields
####### Finish import Marshal#########

class PackageResources(Resource):

    # Untuk tambah actual stock
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("packageActualStocksID", type=int, location="json", required=True, help="packageActualStocksID must be integer and exist")
        parser.add_argument("actual_stock", type=int, location="json", required=False, help="actual_stock must be integer")
        parser.add_argument("notes", type=str, location="json", required=False, help="notes must be string")
        args = parser.parse_args()
        my_identity = get_jwt_identity()
        add_actualstock = ActualStock(
            userActualStocksID = my_identity,
            packageActualStocksID = args['packageActualStocksID'],
            actual_stock = args['actual_stock'],
            notes= args['notes']
        )

        db.session.add(add_actualstock)
        db.session.commit()
        
        return {
            "message": "add actual stock success",
            "actual stock": marshal(add_actualstock, actualstock_fields)
        }, 200

    # untuk edit actual stock
    @jwt_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('packageActualStocksID', type = int, help='packageActualStocksID must be integer type', location='json')
        parser.add_argument('actual_stock', type = int, help='actual_stock must be integer type', location='json')
        parser.add_argument('notes', type = str, help='notes must be string type', location='json')

        args = parser.parse_args()
        
        qry = ActualStock.query.filter_by(id = id).first()
        
        if qry == None :
            return {'message': 'actual stock not found'}, 404

        else:
            if args["packageActualStocksID"] != None:
                qry.packageActualStocksID= args["packageActualStocksID"]
            if args["actual_stock"] != None:
                qry.actual_stock= args["actual_stock"]
            if args["notes"] != None:
                qry.notes= args["notes"]

            qry.updated_at = db.func.current_timestamp()
                    
            db.session.add(qry)
            db.session.commit()

            return {
                "message": "edit actual stock success",
                "actual stock": marshal(qry, actualstock_fields)
            } ,200

    # Untuk hapus actual stock
    @jwt_required
    def delete(self, id):
        
        qry = ActualStock.query.filter_by(id = id).first()

        if qry == None:
            return {'message': "actual stock not found!"}, 404

        db.session.delete(qry)
        db.session.commit()

        return {'message': "delete actual stock success"}, 200

    # Untuk menampilkan actual stock
    @jwt_required
    def get(self, id=None):

        my_identity = get_jwt_identity()

        qry = ActualStock.query

        #   get by id

        if id != None:
            qry = qry.filter_by(userActualStocksID = my_identity).filter_by(id = id)

            rows = []

            for row in qry.all():
                rows.append(marshal(row, actualstock_fields))

            if rows == []:
                return {'message': 'actual stock not found'}, 404

            return {
                "message": "success",
                "package": rows
            }, 200

        # get all

        qry = qry.filter_by(userActualStocksID = my_identity)

        rows = []

        for row in qry.all():
            rows.append(marshal(row, actualstock_fields))

        if rows == []:
            return {'message': 'actual stock not found'}, 404

        return {
            "message": "success",
            "packages": rows
        }, 200