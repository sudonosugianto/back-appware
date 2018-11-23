from flask_restful import fields

# user_field = {
#     'client_id' : fields.Integer,
#     'client_key' : fields.String,
#     'client_secret' : fields.String,
#     'status' : fields.Boolean,
#     'type':fields.String
# }

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