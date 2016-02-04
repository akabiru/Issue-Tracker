from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_required, current_user
from . import issue
from .. import db
from ..models import Issue
from .forms import IssueForm


@issue.route('/issue')
@login_required
def index():
    '''This view function displays
    issues records in the database.
    '''
    issues_ = Issue.query.all()
    closed_issues = 0
    open_issues = 0

    for i in issues_:
        if i.closed:
            closed_issues += 1
        else:
            open_issues += 1
    total_issues = len(issues_)
    return render_template('issue/index.html', issues_=issues_,
                           total_issues=total_issues,
                           closed_issues=closed_issues,
                           open_issues=open_issues)


@issue.route('/issue/new', methods=['GET', 'POST'])
@login_required
def issue():
    '''This view function creates a
    new issue record
    '''
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
        return redirect(request.args.get('next') or url_for('issue.index'))
    return render_template('issue/new_issue.html', form=form)
