from models import db

class PODetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    #Foreign key field
    POID = db.Column(db.Integer, db.ForeignKey("PO.id", ondelete='CASCADE'), nullable=False)
    packageID = db.Column(db.Integer, db.ForeignKey('packages.id', ondelete='CASCADE'), nullable = False)
    
    #Field
    packageName = db.Column(db.String(255))
    inStock = db.Column(db.Integer, default = 0)
    order = db.Column(db.Integer,default = 0)
    unitCost = db.Column(db.Float, default=0)
    subTotal = db.Column(db.Float, default=0)
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    def __repr__(self):
        return "<PODetails %r>" % self.id