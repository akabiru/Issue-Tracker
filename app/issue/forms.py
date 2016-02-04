from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SelectField
from wtforms import SubmitField, validators
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Department


class IssueForm(Form):
    '''This class creates an IssueForm
    object.
    '''

    name = StringField('Issue',
                       [validators.Required(message='We need an issue.'),
                        validators.Length(
                           max=70,
                           message='Your \subject is a tad long.'
                       )
                       ]
                       )
    description = TextAreaField('Issue Description',
                                [validators.required(
                                    message='Please describe your issue.')])
    priority = SelectField('Priority', choices=[
        ('high', 'High'), ('medium', 'Medium'), ('low', 'Low')])
    department = SelectField('Department',
                             [validators.Required(
                                 message='Department required.')],
                             coerce=int)
    submit = SubmitField('Post Issue')

    def __init__(self, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        self.department.choices = [
            (dept.id, dept.name) for dept in Department.query.all()]


class CommentForm(Form):
  '''This class creates a CommentForm
  object
  '''
  comment = TextAreaField('Comment')