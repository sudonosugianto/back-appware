from models import db

class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    userSalesID = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    customerSalesID = db.Column(db.Integer, db.ForeignKey('customers.id', ondelete='CASCADE'), nullable = False)
    stockSalesID = db.Column(db.Integer, db.ForeignKey('stocks.id', ondelete='CASCADE'), nullable = False)
    # field
    quantity = db.Column(db.Integer, nullable=False)
    sellingPrice = db.Column(db.Float, nullable=False)
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    def __repr__(self):
        return "<Sales %r>" % self.id