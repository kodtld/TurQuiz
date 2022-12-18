"""
Form for creating an individual question for a quiz
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length

class QuestionForm(FlaskForm):
    """
    Form for creating an individual question for a quiz
    """
    question_1 = StringField('question_1', validators=[InputRequired(), Length(min=4,max=120)],
        render_kw={'placeholder': 'Question...'})
    q1_answer = StringField('q1_answer', validators=[InputRequired(), Length(min=4,max=50)],
        render_kw={'placeholder': 'The right answer...'})
    q1_option_1 = StringField('q1_option_1', validators=[InputRequired(), Length(min=4,max=50)],
        render_kw={'placeholder': 'Wrong option 1...'})
    q1_option_2 = StringField('q1_option_2', validators=[InputRequired(), Length(min=4,max=50)],
        render_kw={'placeholder': 'Wrong option 2...'})
    q1_option_3 = StringField('q1_option_3', validators=[InputRequired(), Length(min=4,max=50)],
        render_kw={'placeholder': 'Wrong option 3...'})
