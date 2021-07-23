from flask import render_template
from .poll_app import app


@app.route('/')
def home_page():
    return render_template('homepage.html')
