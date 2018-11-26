from models import db

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    userCustomerID = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    # field
    fullname = db.Column(db.String(50), nullable=False)
    phoneNumber = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable = False)
    address = db.Column(db.String(500))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zipcode = db.Column(db.String(50))
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    # relationship
    sales = db.relationship('Sales', backref='customers', lazy=True)

    def __repr__(self):
        return "<Customers %r>" % self.id