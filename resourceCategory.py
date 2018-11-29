from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
import datetime

from models import db
####### Tempat import Model#########
from modelCat import Category
####### Finish import Model#########

####### Tempat import Model#########
from marshalField import category_fields
####### Finish import Model#########

class CategoryResources(Resource):
    # Untuk Create Item
    @jwt_required
    def post(self):
        userID = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument("category", type=str, location="json", help="CategoryID must Exist")
        args = parser.parse_args()
        add_category = Category(
            userID = userID,
            category = args['category']
        )
        db.session.add(add_category)
        db.session.commit() 
        return {
            "message": "add Category success",
            "category": marshal(add_category, category_fields)
        }, 200