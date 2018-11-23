from models import db
# from modelUsers import Users
from modelCat import Category

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userItem = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False) 
    catID = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False, default="Uncategorized") 
    item = db.Column(db.String(50), nullable=False)
    picture = db.Column(db.String(50), nullable=True)
    size = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(50), nullable=True)
    SKU =  db.Column(db.Integer, nullable=True)
    status = db.Column(db.Boolean, default=1)

    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    
    def __repr__(self):
        return "<Items %r>" % self.id