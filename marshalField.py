from flask_restful import fields

user_field = {
    'client_id' : fields.Integer,
    'client_key' : fields.String,
    'client_secret' : fields.String,
    'status' : fields.Boolean,
    'type':fields.String
}