from flask_restful import fields

user_fields = {
    "id": fields.Integer,
    "fullname": fields.String, 
    "username": fields.String,
    "email": fields.String,
    "phone_number": fields.String,
    "status":fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String
}

item_fields = {
    "id":fields.Integer,
    "userID":fields.Integer,
    "catID": fields.Integer,
    "item":fields.String,
    "picture":fields.String,
    "size":fields.Integer,
    "unit":fields.String,
    "SKU":fields.Integer,
    "status":fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String
}

category_fields = {
    "id":fields.Integer,
    "userID":fields.Integer,
    "category": fields.String,
    "status":fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String
}

package_fields = {
    "id": fields.Integer,
    "itemID": fields.Integer,
    "package_name": fields.String,
    "Items.item": fields.String,
    "items_quantity": fields.Integer,
    "status": fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String,
    "Users.fullname": fields.String,
    "Items.category.category": fields.String
}

supplier_fields = {
    "id": fields.Integer,
    "userSuppliersID": fields.Integer,
    "name" : fields.String,
    "phone_number" : fields.String,
    "email" : fields.String,
    "address" : fields.String,
    "city" : fields.String,
    "state" : fields.String,
    "zipcode" : fields.String,
    "created_at": fields.String,
    "updated_at": fields.String
}