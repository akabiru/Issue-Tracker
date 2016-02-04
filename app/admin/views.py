from flask import render_template
from flask.ext.login import login_required
from . import admin
# from .. import db
from ..models import Issue, User, Department
# from .forms import IssueForm


@admin.route('/users')
@login_required
def users():
    '''View function to return all users.
    '''
    users_ = User.query.all()
    return render_template('admin/users.html', users_=users_)


@admin.route('/issues')
@login_required
def issues():
    issues_ = Issue.query.all()
    return render_template('admin/issues.html', issues_=issues_)


@admin.route('/departments')
def departments():
    departments_ = Department.query.all()
    return render_template('admin/departments.html',
                           departments_=departments_)
