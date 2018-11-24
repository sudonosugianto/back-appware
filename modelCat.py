from models import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    category = db.Column(db.String(50), unique = True)
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    
    # relationship
    items =  db.relationship('Items', backref='Category', lazy=True)
    packages =  db.relationship('Packages', backref='Category', lazy=True)

    def __repr__(self):
        return "<Category %r>" % self.id