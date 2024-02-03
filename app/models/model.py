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
    
class Gender(db.Model):
    __tablename__ = 'gender'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    
    def __init__(self, name):
        self.name = name
        
class MaritalStatus(db.Model):
    __tablename__ = 'marital_status'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    
    def __init__(self, name):
        self.name = name
        
class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    
    def __init__(self, name):
        self.name = name
    
class Employees(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    role = db.Column(db.String(45), nullable=False)
    department = db.Column(db.String(45), nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'))
    gender = db.relationship('Gender', backref=db.backref('employees', lazy=True))
    birth_date = db.Column(db.Date)
    admission_date = db.Column(db.Date)
    resignation_date = db.Column(db.Date, nullable=True)
    #address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    marital_status_id = db.Column(db.Integer, db.ForeignKey('marital_status.id'))
    marital_status = db.relationship('MaritalStatus', backref=db.backref('employees', lazy=True))
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
    status = db.relationship('Status', backref=db.backref('employees', lazy=True))
    
    # no init retirei o address
    def __init__(self, name, phone, email, role, department, gender_id, birth_date, admission_date, resignation_date, marital_status_id, status_id):
        self.name = name
        self.phone = phone
        self.email = email
        self.role = role
        self.department = department
        self.gender_id = gender_id
        self.birth_date = birth_date
        self.admission_date = admission_date
        self.resignation_date = resignation_date
        #self.address_id = address_id
        self.marital_status_id = marital_status_id
        self.status_id = status_id
        


    

    

    


        