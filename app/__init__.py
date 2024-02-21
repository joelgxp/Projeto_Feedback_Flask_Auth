from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'

app.config['SECRET_KEY'] = 'super-secret-key'

login_manager = LoginManager(app)
db = SQLAlchemy(app)

app.config['MESSAGE_FLASHING_OPTIONS'] = {'duration': 3}
