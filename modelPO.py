from models import db

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

    # Backref
    POdetails = db.relationship('PODetails', backref='po', lazy=True)
    def __repr__(self):
        return "<PO %r>" % self.id

