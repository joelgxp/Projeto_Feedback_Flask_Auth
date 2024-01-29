from app import db
from flask_login import UserMixin

import hashlib

    
class Lider(db.Model, UserMixin):
    __tablename__ = 'lideres'
    id_lider = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome_lider = db.Column(db.String(80), nullable=False)
    departamento_lider = db.Column(db.String(80), nullable=False)
    email_lider = db.Column(db.String(120), unique=True, nullable=False)
    password_lider = db.Column(db.String(128), nullable=False)
    ativo_lider = db.Column(db.Boolean, default=True)
    
    def __init__(self, nome_lider, departamento_lider, email_lider, password_lider):
        self.nome_lider = nome_lider
        self.departamento_lider = departamento_lider
        self.email_lider = email_lider
        self.password_lider = self.hash_password(password_lider)
        
    def hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    def verify_password(self, password):
        return self.password_lider == self.hash_password(password)
    
    def get_id(self):
        return self.id_lider

    

    

    


        