"""
Form for creating a quiz
"""
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, Length

class QuizForm(FlaskForm):
    """
    Form for creating a quiz
    """
    subject = StringField('subject', validators=[InputRequired(), Length(min=4,max=25)],
        render_kw={'placeholder': 'Subject of quiz...'})
    private = BooleanField("I want this quiz to be private")
