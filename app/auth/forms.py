from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms import BooleanField, SubmitField, ValidationError, validators
from ..models import User


class LoginForm(Form):
    '''This class creates creates a
    Login form
    '''
    username = StringField('Username',
                           [validators.Required(
                            message='We need your username')]
                           )
    password = PasswordField('Password', [validators.Required()])
    remember = BooleanField('Keep me logged in.')
    submit = SubmitField('Log In')


class RegistrationForm(LoginForm):
    '''This class extends the Login form and
    creates a user registration form.
    '''
    email = StringField(
        'Email Address',
        [
            validators.Required(),
            validators.Length(
                min=6, max=64, message='Your email is invalid')
        ]
    )
    password = PasswordField('Password', [validators.Required(),
                                          validators.EqualTo(
        'password_confirmation',
        'Passwords do not match.'
    )])
    password_confirmation = PasswordField('Password Confirmation',
                                          [validators.Required()])
    first_name = StringField('First Name', [validators.Required()])
    last_name = StringField('Last Name', [validators.Required()])
    submit = SubmitField('Submit')
    remember = None

    def validate_username(self, field):
        '''This method checks if a username already exists in
        the database
        '''
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exists.')
