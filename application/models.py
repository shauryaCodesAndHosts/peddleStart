from .database import db
from flask_login import UserMixin

class users(db.Model, UserMixin):
    __tablename__ = 'users'
    Name = db.Column(db.Integer, nullable= False, primary_key=True,autoincrement= True,)
    Id = db.Column(db.String, nullable=False, unique=True)
    Password= db.Column(db.String, nullable=True,unique=True )
    Notes= db.Column(db.String, nullable=True,unique=True )

    def get_id(self):
       return (self.managerId)
    
