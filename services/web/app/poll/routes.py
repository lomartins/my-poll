from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user

from .forms import get_poll_form
from .. import db
from ..models import Poll, Choice, Vote

blueprint = Blueprint('Polls', __name__)


@blueprint.route('/poll/<int:poll_id>', methods=['GET', 'POST'])
def poll_page(poll_id):
    poll = Poll.query.get(poll_id)
    choices = Choice.query.filter_by(poll_id=poll_id).order_by(Choice.id.asc()).all()

    for index, choice in enumerate(choices):
        choices[index] = (choice.id, choice.choice)

    form = get_poll_form(choices, formdata=request.form)

    if form.validate_on_submit():
        choice_id = form.choice.data

        user_id = None
        if current_user.is_authenticated:
            user_id = current_user.id

        # update choice votes and save to database
        choice = Choice.query.get(choice_id)
        choice.votes += 1
        db.session.commit()
        # create new vote
        vote = Vote(choice_id=choice_id, user_id=user_id)
        db.session.add(vote)
        db.session.commit()
        flash('Vote Submitted')
        return redirect(url_for('Polls.poll_page', poll_id=poll_id))

    return render_template('poll/poll.html', poll_id=poll_id, poll=poll, form=form)
