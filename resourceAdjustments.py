from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime


from models import db


####### Tempat import Model#########
from modelAdjustments import Adjustments
####### Finish import Model#########


####### Tempat import Marshal#########
from marshalField import adjustment_fields
####### Finish import Marshal#########


class AdjustmentResources(Resource):

    # Untuk tambah adjustment
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("stockAdjustmentsID", type=int, location="json", required=True, help="stockAdjustmentsID must be integer and exist")
        parser.add_argument("actualStocks", type=int, location="json", help="actualStocks must be integer")
        parser.add_argument("notes", type=str, location="json", help="notes must be string")

        args = parser.parse_args()

        my_identity = get_jwt_identity()

        add_adjustment = Adjustments(
            userAdjustmentsID = my_identity,
            stockAdjustmentsID = args['stockAdjustmentsID'],
            actualStocks= args['actualStocks'],
            notes= args['notes']
        )

        db.session.add(add_adjustment)
        db.session.commit()
        
        return {
            "message": "add adjustment success",
            "adjustment": marshal(add_adjustment, adjustment_fields)
        }, 200

    # untuk edit adjustment
    @jwt_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("userAdjustmentsID", type=int, location="json", help="userAdjustmentsID must be integer")
        parser.add_argument("stockAdjustmentsID", type=int, location="json", help="stockAdjustmentsID must be integer")
        parser.add_argument("actualStocks", type=int, location="json", help="actualStocks must be integer")
        parser.add_argument("notes", type=str, location="json", help="notes must be string")

        args = parser.parse_args()

        my_identity = get_jwt_identity()
        
        qry = Adjustments.query.filter_by(userAdjustmentsID = my_identity).filter_by(id = id).first()
        
        if qry == None :
            return {'message': 'adjustment not found'}, 404

        else:
            if args["userAdjustmentsID"] != None:
                qry.userAdjustmentsID= args["userAdjustmentsID"]
            if args["stockAdjustmentsID"] != None:
                qry.stockAdjustmentsID= args["stockAdjustmentsID"]
            if args["actualStocks"] != None:
                qry.actualStocks= args["actualStocks"]
            if args["notes"] != None:
                qry.notes= args["notes"]

            qry.updated_at = db.func.current_timestamp()
                    
            db.session.add(qry)
            db.session.commit()

            return {
                "message": "edit adjustment success",
                "adjustments": marshal(qry, adjustment_fields)
            } ,200

    @jwt_required
    def delete(self, id):

        my_identity = get_jwt_identity()
        
        qry = Adjustments.query.filter_by(userAdjustmentsID = my_identity).filter_by(id = id).first()

        if qry == None:
            return {'message': "adjustment not found!"}, 404

        db.session.delete(qry)
        db.session.commit()

        return {'message': "delete adjustment success"}, 200

    # menampilkan sales
    @jwt_required
    def get(self, id=None):

        my_identity = get_jwt_identity()

        qry = Adjustments.query

        #   get by id

        if id != None:
            qry = qry.filter_by(userAdjustmentsID = my_identity).filter_by(id = id)

            rows = []

            for row in qry.all():
                rows.append(marshal(row, adjustment_fields))

            if rows == []:
                return {'message': 'adjustment not found'}, 404

            return {
                "message": "success",
                "adjustment": rows
            }, 200

        # get all

        rows = []

        for row in qry.all():
            rows.append(marshal(row, adjustment_fields))

        if rows == []:
            return {'message': 'adjustment not found'}, 404

        return {
            "message": "success",
            "adjustments": rows
        }, 200