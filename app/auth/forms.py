from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from ..models import User

# Registration form

class RegistrationForm(FlaskForm):

    fullname = StringField('Enter Your full Name', validators=[DataRequired()])
    email = EmailField('Enter your email', validators=[DataRequired()])
    role = StringField('Enter Your current role', validators=[DataRequired()])
    password = PasswordField('Enter Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords do not match')])
    submit = SubmitField('Create account')

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('Email is already in use')

class LoginForm(FlaskForm):

    email = EmailField('Enter your email : ', validators=[DataRequired()])
    password = PasswordField('Enter Password :', validators=[DataRequired()])
    remember = BooleanField('Remember me')

    submit = SubmitField('Login')

    
