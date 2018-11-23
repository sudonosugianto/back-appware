from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime

from models import db
####### Tempat import Model#########
from modelItems import Items
####### Finish import Model#########

####### Tempat import Model#########
from marshalField import item_fields
####### Finish import Model#########

class ItemResources(Resource):
    # Untuk Create Item
    @jwt_required
    def post(self):
        userItem = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument("catID", type=int, location="json", help="CategoryID must Exist")
        parser.add_argument("item", type=str, location="json", required=True, help="Item must be string and exist")
        parser.add_argument("picture", type=str, location="json", required=False, help="Picture must be string and exist")
        parser.add_argument("size", type=int, location="json", required=True, help="Size must be integer")
        parser.add_argument("SKU", type=int,location="json",required = False, help="Stock Keeping Unit must be Integer")
        args = parser.parse_args()

        add_item = Items(
            userItem = userItem,
            catID = args['catID'],
            item= args['item'],
            picture= args['picture'],
            size= args['size'],
            SKU = args['SKU']
        )
        db.session.add(add_item)
        db.session.commit() 
        return {
            "message": "add Item success",
            "item": marshal(add_item, item_fields)
        }, 200