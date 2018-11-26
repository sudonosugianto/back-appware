from models import db

class PO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    supplierID = db.Column(db.Integer, db.ForeignKey("suppliers.id", ondelete='CASCADE'), nullable=False)
    userPOID = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable = False)
    packagePOID = db.Column(db.Integer, db.ForeignKey("packages.id", ondelete='CASCADE'), nullable = False)
    # field
    quantity = db.Column(db.Integer, nullable=False, default=0)
    buyingPricePerPackage = db.Column(db.Float, default=0)
    totalPrice = db.Column(db.Float, default=0)
    notes = db.Column(db.String(255))
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    # Backref
    def __repr__(self):
        return "<PO %r>" % self.id

