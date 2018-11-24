from models import db
# from models import Items

class Packages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    itemID = db.Column(db.Integer, db.ForeignKey("items.id", ondelete='CASCADE'), nullable=False)
    userPackageID = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable = False)
    catPackageID = db.Column(db.Integer, db.ForeignKey('category.id',ondelete='CASCADE'),nullable=False, default=1) 
    # field
    package_name = db.Column(db.String(50), nullable=False, unique=True)
    items_quantity = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    def __repr__(self):
        return "<Packages %r>" % self.id