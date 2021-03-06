from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request


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
        parser.add_argument("category", type=str, location="json", help="Category must Exist")
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
    
    @jwt_required
    def put(self, id=None):
        userID = get_jwt_identity()
        
        parser = reqparse.RequestParser()
        parser.add_argument("category", type=str, location="json", help="CategoryID must Exist")
        args = parser.parse_args()

        qry = Category.query.filter_by(id=id).first()
        if args['category'] != None:
            qry.category = args['category']

        qry.updated_at = db.func.current_timestamp()

        db.session.add(qry)
        db.session.commit() 
        return {
            "message": "Edit Category success",
            "item": marshal(qry, category_fields)
        }, 200

    @jwt_required
    def delete(self,id=None):
        qry = Category.query.get(ident=id)

        if qry == None :
            return {"message":"Category Not Found"}, 404

        db.session.delete(qry)
        db.session.commit()

        return {"message":"Delete Category Successfull"}, 200

    @jwt_required
    def get(self,id=None):
        userID = get_jwt_identity()
        qry = Category.query
        parser = reqparse.RequestParser()
        parser.add_argument("search", type=str, location="args", help="search must string")
        parser.add_argument('orderBy',location='args',help='invalid order by',choices=("category"))
        parser.add_argument('sort',location='args',help='invalid sort',choices=('desc','asc'))
        args = parser.parse_args()

        if id is None :
            if args['search'] is not None:
                search = args['search']
                # Fungsi untuk search, digunakan filter daripada filter_by 
                # karena butuh method like dengan regex %
                qry = qry.filter_by(userID=userID)\
                                    .filter(Category.category.like('%'+search+'%')).order_by(Category.category)

            if args["sort"] is not None:
                sort = args['sort']
                if args['orderBy']=='category':
                    qry=qry.order_by('category %s'%(sort)).order_by(Category.category)

            if qry is None:
                return{"message":"Search not Found"}, 404
            
            else:
                # Query untuk mendapatkan semua kategori
                qry = qry.filter_by(userID=userID).order_by(Category.category).all()
            return {"message":"Search Result",
                    "category":marshal(qry,category_fields)}, 200
        else :
            qry = Category.query.get(ident=id)
        return {"message":"All Category from user",
                "category":marshal(qry,category_fields)}, 200