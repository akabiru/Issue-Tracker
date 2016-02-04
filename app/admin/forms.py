from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, validators, SelectField
from wtforms import IntegerField
from ..models import User


class DepartmentForm(Form):
    '''This class creates a new Department
    Form object
    '''
    name = StringField('Department Name', [validators.Required()])
    dept_head = SelectField('Department Head', coerce=int)    
    submit = SubmitField('Create Department')

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.dept_head.choices = [
            (user.id, user.username) for user in User.query.all()
        ]
