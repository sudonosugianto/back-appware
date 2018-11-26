from models import db

# Tempat Import Model Database #
from modelItems import Items

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
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
    adjustments = db.relationship("Adjustments", backref="Users", lazy=True)
    stocks = db.relationship("Stocks", backref="Users", lazy=True)

    def __repr__(self):
        return "<Users %r>" % self.id