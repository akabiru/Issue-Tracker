from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_required, current_user
from . import issue
from .. import db
from ..models import Issue
from .forms import IssueForm


@issue.route('/issue')
def index():
    issues_ = Issue.query.all()
    issues_len = len(issues_)
    return render_template('issue/index.html', issues_=issues_,
                           issues_len=issues_len)


@issue.route('/issue/new', methods=['GET', 'POST'])
@login_required
def issue():
    form = IssueForm()
    if form.validate_on_submit():
        user = current_user.id
        issue_ = Issue(name=form.name.data,
                       description=form.description.data,
                       priority=form.priority.data,
                       user_id=user)
        # import ipdb; ipdb.set_trace()
        db.session.add(issue_)
        db.session.commit()
        flash('Issue posted successfully.')
        return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('issue/new_issue.html', form=form)
