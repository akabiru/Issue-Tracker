from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, IntegerField
from wtforms import SubmitField, validators


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
    priority = IntegerField('Priority')
    submit = SubmitField('Post Issue')
