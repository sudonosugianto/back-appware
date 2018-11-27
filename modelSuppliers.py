from models import db

class Suppliers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    userSuppliersID = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    # field
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    address = db.Column(db.String(255))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zipcode = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    PO = db.relationship('PO', backref='suppliers', lazy=True)
    def __repr__(self):
        return "<Packages %r>" % self.id