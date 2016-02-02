from flask import render_template
from flask.ext.login import login_required
from . import main


@main.route('/')
@login_required
def index():
    return render_template('index.html')
