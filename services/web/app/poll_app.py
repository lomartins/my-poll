import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

POSTGRES_USER = os.getenv('POSTGRES_USER', 'development')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'development')
SALT_KEY = os.getenv('SALT_KEY', 'development')
SECRET_KEY = os.getenv('SECRET_KEY', 'development_key')
POSTGRES_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/poll_app'

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
