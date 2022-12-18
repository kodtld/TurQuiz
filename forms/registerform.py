"""
Form for registering a new user
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length

class RegisterForm(FlaskForm):
    """
    Form for registering a new user
    """
    username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)],
        render_kw={'placeholder': 'Username...'})
    email = StringField('email', validators=[InputRequired(), Email('Invalid email'),
        Length(max=50)], render_kw={'placeholder': 'Email...'})
    password = PasswordField('password', validators=[InputRequired(), Length(min=8,max=80)],
        render_kw={'placeholder': 'Password...'})
