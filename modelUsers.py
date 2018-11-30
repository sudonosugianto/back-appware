from models import db
from werkzeug.security import generate_password_hash, check_password_hash

# Tempat Import Model Database #
from modelItems import Items

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable = False)
    phone_number = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    # relationship
    Items = db.relationship('Items', backref='users', lazy=True)
    packages =  db.relationship('Packages', backref='Users', lazy=True)
    suppliers = db.relationship('Suppliers',backref='Users', lazy=True)
    customers = db.relationship("Customers", backref="Users", lazy=True)
    sales = db.relationship("Sales", backref="Users", lazy=True)
    po = db.relationship("PO", backref="users", lazy=True)
    actualstocks = db.relationship("ActualStock", backref="users", lazy=True)

    def __repr__(self):
        return "<Users %r>" % self.id