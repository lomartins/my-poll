from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField


def get_poll_form(choices=0, coerce=int, **kwargs):
    class PollForm(FlaskForm):
        submit = SubmitField('Submit')
        choice = RadioField('Choice', choices=choices, coerce=coerce)

    return PollForm(**kwargs)
