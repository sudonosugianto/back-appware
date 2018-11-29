from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
from sqlalchemy import or_

from models import db
####### Tempat import Model#########
from modelItems import Items
from modelCat import Category
####### Finish import Model#########

####### Tempat import Model#########
from marshalField import item_fields
####### Finish import Model#########

class ItemResources(Resource):
    # Untuk Menampilkan Item
    @jwt_required
    def get(self,id=None):

        my_identity = get_jwt_identity()

        qry = Items.query.join(Category, Category.id == Items.catID).filter(Items.userID == my_identity)
        
        parser = reqparse.RequestParser()
        parser.add_argument("catID", type=int, location="args", help="catID must be integer")
        parser.add_argument("search", type=str, location="args", help="search must be string")
        args = parser.parse_args()

        if id is None :
            qry =qry.order_by(Items.item)
            # by Category
            if args['catID'] is not None:
                qry = qry.filter_by(catID = args['catID']).order_by(Items.item)

            # by item or category
            if args['search'] is not None:
                search = args["search"]
                qry = qry.filter(or_(Category.category.like('%'+search+'%'),Items.item.like('%'+search+'%'))).order_by(Items.item)

        #     # Untuk get all tanpa kategori
        #     if args['category'] is None:
        #         qry = Items.query.filter_by(userID = my_identity).all()
        #     else:
        #         qry = Items.query.join(Category, Items.catID == Category.id)\
        #                         .filter(Category.category == args['category'])\
        #                         .filter(Items.userID == my_identity).all()

        else:
            qry = qry.filter(Items.id == id)

        rows = []

        for row in qry.all():
            rows.append(marshal(row, item_fields))

        if rows == []:
            return {'message': 'items not found'}, 404

        return {"message":"Display Item Success",
                "item": rows}, 200

    @jwt_required
    def post(self):
        userID = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument("catID", type=int, location="json", help="CategoryID must Exist")
        parser.add_argument("item", type=str, location="json", required=True, help="Item must be string and exist")
        parser.add_argument("picture", type=str, location="json", required=False, help="Picture must be string and exist")
        parser.add_argument("size", type=int, location="json", required=True, help="Size must be integer")
        parser.add_argument("unit", type=str, location="json", required=False, help="Unit must be String")
        parser.add_argument("SKU", type=str,location="json",required = False, help="Stock Keeping Unit must be Integer")
        args = parser.parse_args()
        add_item = Items(
            userID = userID,
            catID = args['catID'],
            item= args['item'],
            picture= args['picture'],
            size= args['size'],
            unit= args['unit'],
            SKU = args['SKU']
        )
        db.session.add(add_item)
        db.session.commit() 
        return {
            "message": "add Item success",
            "item": marshal(add_item, item_fields)
        }, 200
    
    @jwt_required
    def put(self,id=None):
        # userID = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument("catID", type=int, location="json", help="CategoryID must Exist")
        parser.add_argument("item", type=str, location="json", required=True, help="Item must be string and exist")
        parser.add_argument("picture", type=str, location="json", required=False, help="Picture must be string and exist")
        parser.add_argument("size", type=int, location="json", required=True, help="Size must be integer")
        parser.add_argument("unit", type=str, location="json", required=False, help="Unit must be String")
        parser.add_argument("SKU", type=str,location="json",required = False, help="Stock Keeping Unit must be Integer")
        args = parser.parse_args()

        qry = Items.query.filter_by(id=id).first()
        if args['catID'] != None:
            qry.catID = args['catID']
        if args['item'] != None:
            qry.item = args['item']
        if args['picture'] != None:
            qry.picture = args['picture']
        if args['size'] != None:
            qry.size = args['size']
        if args['unit'] != None:
            qry.unit = args['unit']
        if args['SKU'] != None:
            qry.SKU = args['SKU']
        
        qry.updated_at = db.func.current_timestamp()
        
        db.session.add(qry)
        db.session.commit() 
        return {
            "message": "add Item success",
            "item": marshal(qry, item_fields)
        }, 200

    @jwt_required
    def delete(self,id=None):
        qry = Items.query.get(ident=id)

        if qry == None :
            return {"message":"Items Not Found"}, 404
            
        db.session.delete(qry)
        db.session.commit()

        return {"message":"Delete Items Successfull"}, 200