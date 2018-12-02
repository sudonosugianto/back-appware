from models import db

class PackagesTrack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    POID = db.Column(db.Integer, db.ForeignKey("PO.id", ondelete='CASCADE'), nullable=False)
    salesID = db.Column(db.Integer, db.ForeignKey("sales.id", ondelete='CASCADE'))
    packageID = db.Column(db.Integer, db.ForeignKey("packages.id", ondelete='CASCADE'), nullable = False)
    # field
    code = db.Column(db.String(255))
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    def __repr__(self):
        return "<PO %r>" % self.id

