from models import db

class ActualStock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    userActualStocksID = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    packageActualStocksID = db.Column(db.Integer, db.ForeignKey("packages.id", ondelete='CASCADE'), nullable=False)
    # field
    actual_stock = db.Column(db.Integer, default=0)
    notes = db.Column(db.String(1000))
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    def __repr__(self):
        return "<ActualStock %r>" % self.id

