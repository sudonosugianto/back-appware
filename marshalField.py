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

package_fields = {
    "id": fields.Integer,
    "itemID": fields.Integer,
    "package_name": fields.String,
    "items_quantity": fields.Integer,
    "status": fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String,
    "items.users.fullname": fields.String,
    "items.category.category": fields.String
}