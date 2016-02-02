from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import ValidationError
from wtforms.validators import Required, EqualTo
from ..models import User


class LoginForm(Form):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required(),
                                                     EqualTo(
        'password_confirmation',
        'Passwords do not match.'
    )])
    password_confirmation = PasswordField('Password Confirmation',
                                          validators=[Required()])
    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exists.')
