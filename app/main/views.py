from flask import render_template
from ..models import Issue
from . import main


@main.route('/')
def index():
    issues = Issue.query.count()
    return render_template('index.html', issues=issues)
