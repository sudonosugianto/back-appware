from models import db
# from models import Items

class Packages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    itemID = db.Column(db.Integer, db.ForeignKey("items.id", ondelete='CASCADE'), nullable=False)
    userPackageID = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    catPackageID = db.Column(db.Integer, db.ForeignKey('category.id',ondelete='CASCADE')) 
    # field
    package_name = db.Column(db.String(50), nullable=False)
    items_quantity = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    # Backref
    ActualStock = db.relationship('ActualStock', backref='packages', lazy=True)
    PO = db.relationship('PO', backref='packages', lazy=True)
    Sale = db.relationship('Sales', backref='packages', lazy=True)
    def __repr__(self):
        return "<Packages %r>" % self.id