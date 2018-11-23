from models import db
from models import Items

class Packages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    itemID = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=False)
    # field
    package_name = db.Column(db.String(50), nullable=False)
    items_quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    def __repr__(self):
        return "<Packages %r>" % self.id