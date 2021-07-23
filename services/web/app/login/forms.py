from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators

from ..models import User


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Submit')

    def validate(self):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(name=self.username.data).first()
        if not user:
            self.submit.errors.append('Invalid username or password')
            return False
        if not user.verify_password(self.password.data):
            self.submit.errors.append('Invalid username or password')
            return False
        return True


class SignUpForm(FlaskForm):
    username = StringField('Username')
    email = StringField(
        label='Email',
        validators=[validators.DataRequired('Please enter your email address.'),
                    validators.Email('Please enter a valid email address.'), ]
    )

    password = PasswordField('Password')
    submit = SubmitField('Submit')

    def validate(self):
        initial_validation = super(SignUpForm, self).validate()
        if not initial_validation:
            return False

        # TODO: add password validation

        return True
