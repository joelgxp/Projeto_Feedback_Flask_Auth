from app import db
from flask_login import UserMixin

import hashlib

    
class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    access_level = db.Column(db.String(45))
    
    def __init__(self, name, email, pwd, access_level):
        self.name = name
        self.email = email
        self.password = self.hash_password(pwd)
        self.access_level = access_level
        
    def hash_password(self, pwd):
        return hashlib.sha256(pwd.encode('utf-8')).hexdigest()
    
    def verify_password(self, pwd):
        password_input = hashlib.sha256(pwd.encode('utf-8')).hexdigest()  
        return password_input == self.password
    
    def get_id(self):
        return self.id

    

    

    


        