from .poll_app import app, db
from . import routes, models
from . import login, poll

app.register_blueprint(login.routes.blueprint)
app.register_blueprint(poll.routes.blueprint)
