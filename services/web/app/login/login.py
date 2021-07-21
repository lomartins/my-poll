from flask_login import LoginManager

from ..poll_app import app
from ..models import User

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
