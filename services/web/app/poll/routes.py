from flask import Blueprint, render_template, request, redirect, url_for

from .. import db
from ..models import Poll, Choice, Vote

blueprint = Blueprint('Polls', __name__)


@blueprint.route('/poll/<int:poll_id>')
def poll_page(poll_id):
    poll = Poll.query.get(poll_id)
    choices = Choice.query.filter_by(poll_id=poll_id).order_by(Choice.id.asc()).all()
    return render_template('poll/poll.html', poll_id=poll_id, poll=poll, choices=choices)


@blueprint.route('/poll/<int:poll_id>/', methods=['POST'])
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
    return redirect(url_for('Polls.poll_page', poll_id=poll_id))
