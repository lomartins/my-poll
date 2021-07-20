import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

POSTGRES_USER = os.getenv('POSTGRES_USER', 'development')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'development')
POSTGRES_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/poll_app'

app = Flask(__name__)
app.secret_key = 'development key'
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def main():
    db.create_all()
    app.run(debug=True)


if __name__ == '__main__':
    main()
