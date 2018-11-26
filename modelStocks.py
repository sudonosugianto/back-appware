from models import db
# from models import Items

class Stocks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    packagesID = db.Column(db.Integer, db.ForeignKey("packages.id", ondelete='CASCADE'), nullable=False)
    userStocksID = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    # field
    beginning = db.Column(db.Integer, default=0)
    PO = db.Column(db.Integer, default=0)
    sale = db.Column(db.Integer, default=0)
    adjustment = db.Column(db.Integer, default=0)
    # ending = db.Column(db.Integer, default=0)
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    # relationship
    sales = db.relationship("Sales", backref="Stocks", lazy=True)
    adjustments = db.relationship("Adjustments", backref="Stocks", lazy=True)

    # backref
    PO = db.relationship('PO', backref='stocks', lazy=True)
    def __repr__(self):
        return "<Stocks %r>" % self.id