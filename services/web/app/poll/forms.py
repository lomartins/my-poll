from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, validators, FieldList


class CreatePollForm(FlaskForm):
    question = StringField('Question', validators=[validators.DataRequired('Please enter your question.')])
    choices = FieldList(StringField('Choice'), min_entries=2)
    submit = SubmitField('Submit')


def get_poll_form(choices=0, coerce=int, **kwargs):
    class PollForm(FlaskForm):
        choice = RadioField('Choice', choices=choices, coerce=coerce)
        submit = SubmitField('Submit')

    return PollForm(**kwargs)
