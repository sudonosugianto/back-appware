from models import db
# from models import Items

class Stocks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    packagesID = db.Column(db.Integer, db.ForeignKey("packagess.id", ondelete='CASCADE'), nullable=False)
    # field
    beginning = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    def __repr__(self):
        return "<PO %r>" % self.id