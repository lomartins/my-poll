from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'development key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:15432/postgres'
db = SQLAlchemy(app)


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


@app.route('/')
def home_page():
    return render_template('homepage.html')


@app.route('/poll/<int:poll_id>')
def poll_page(poll_id):
    poll = Poll.query.get(poll_id)
    choices = Choice.query.filter_by(poll_id=poll_id).order_by(Choice.id.asc()).all()
    return render_template('poll.html', poll_id=poll_id, poll=poll, choices=choices)


@app.route('/poll/<int:poll_id>/', methods=['POST'])
def create_vote(poll_id):
    choice_id = request.form['choice']
    user_id = request.form['user']
    # update choice votes and save to database
    choice = Choice.query.get(choice_id)
    choice.votes += 1
    db.session.commit()
    # create new vote
    vote = Vote(choice_id=choice_id, user_id=user_id)
    db.session.add(vote)
    db.session.commit()
    return redirect(url_for('poll_page', poll_id=poll_id))


def main():
    db.create_all()
    app.run(debug=True)


if __name__ == '__main__':
    main()
