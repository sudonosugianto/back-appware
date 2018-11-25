from models import db
# from models import Items

# PO detail table helper
POdetails = db.Table('POdetails',
    db.Column('POID', db.Integer, db.ForeignKey('PO.id'), primary_key = True),
    db.Column('packageID', db.Integer, db.ForeignKey('packages.id'), primary_key = True),
    db.Column('package_name', db.String(50)),
    db.Column('inStock', db.Integer, default=0),
    db.Column('order', db.Integer, default=0),
    db.Column('unitCost', db.Float, default=0),
    db.Column('subTotal', db.Float, default=0)
)

class PO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    supplierID = db.Column(db.Integer, db.ForeignKey("suppliers.id", ondelete='CASCADE'), nullable=False)
    stockID = db.Column(db.Integer, db.ForeignKey('stocks.id', ondelete='CASCADE'), nullable = False)
    # field
    total = db.Column(db.Float, default=0)
    notes = db.Column(db.String(255))
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    POdetails = db.relationship('Packages', secondary=POdetails, lazy='subquery',backref=db.backref('po', lazy=True))
    def __repr__(self):
        return "<PO %r>" % self.id

