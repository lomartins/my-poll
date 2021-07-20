from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

from .poll_app import app
from .models import User

login_manager = LoginManager()
login_manager.init_app(app)


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
            self.username.errors.append('Unknown username')
            return False
        if not user.verify_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False
        return True


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
