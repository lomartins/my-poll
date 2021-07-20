from datetime import datetime
from .poll_app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password


class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200))
    pub_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, question, pub_date=None):
        self.question = question
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date


class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'))
    choice = db.Column(db.String(200))
    votes = db.Column(db.Integer)

    def __init__(self, poll_id, choice, votes=0):
        self.poll_id = poll_id
        self.choice = choice
        self.votes = votes


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    choice_id = db.Column(db.Integer, db.ForeignKey('choice.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, choice_id, user_id):
        self.choice_id = choice_id
        self.user_id = user_id
