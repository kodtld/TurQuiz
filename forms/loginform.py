from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)], render_kw={'placeholder': 'Username...'})
    password = PasswordField('password', validators=[InputRequired(), Length(min=8,max=80)], render_kw={'placeholder': 'Password...'})
