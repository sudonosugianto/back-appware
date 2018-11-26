from models import db

class Adjustments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    userAdjustmentsID = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    stockAdjustmentsID = db.Column(db.Integer, db.ForeignKey('stocks.id', ondelete='CASCADE'), nullable = False)
    # field
    actualStocks = db.Column(db.Integer, nullable=False, default=0)
    notes = db.Column(db.String(1000))
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    def __repr__(self):
        return "<Adjustments %r>" % self.id