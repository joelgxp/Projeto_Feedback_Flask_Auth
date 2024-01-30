from app import db
from flask_login import UserMixin

import hashlib

    
class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    access_level = db.Column(db.String(45), nullable=False)
    
    def __init__(self, email, password, access_level):
        self.email = email
        self.password = password
        self.password_lider = self.hash_password(password)
        self.access_level = access_level
        
    def hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    def verify_password(self, password):
        return self.password == self.hash_password(password)
    
    def get_id(self):
        return self.id

    

    

    


        