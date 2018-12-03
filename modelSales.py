from models import db

class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    userSalesID = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    customerSalesID = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='CASCADE'), nullable = False)
    packageSalesID = db.Column(db.Integer, db.ForeignKey('packages.id', ondelete='CASCADE'), nullable = False)
    # field
    quantity = db.Column(db.Integer, nullable=False)
    sellingPricePerPackage = db.Column(db.Float, nullable=False)
    totalPrice = db.Column(db.Float)
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    # backref
    PackageTrack = db.relationship("PackagesTrack", backref="sales", lazy=True)
    def __repr__(self):
        return "<Sales %r>" % self.id