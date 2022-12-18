"""
Form for user login
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    """
    Form for user login
    """
    username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)],
        render_kw={'placeholder': 'Username...'})
    password = PasswordField('password', validators=[InputRequired(), Length(min=8,max=80)],
        render_kw={'placeholder': 'Password...'})
