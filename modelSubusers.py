from models import db

class Subusers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreign key field
    userID = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'),nullable=False)
    # field
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50))
    apiKey = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(50))
    subuser_type = db.Column(db.String(50))
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    def __repr__(self):
        return "<Subusers %r>" % self.id