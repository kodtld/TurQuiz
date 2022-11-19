from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length

class QuestionForm(FlaskForm):
    question_1 = StringField('question_1', validators=[InputRequired(), Length(min=4,max=120)], render_kw={'placeholder': 'Question...'})
    q1_answer = StringField('q1_answer', validators=[InputRequired(), Length(min=4,max=50)], render_kw={'placeholder': 'The right answer...'})
    q1_option_1 = StringField('q1_option_1', validators=[InputRequired(), Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 1...'})
    q1_option_2 = StringField('q1_option_2', validators=[InputRequired(), Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 2...'})
    q1_option_3 = StringField('q1_option_3', validators=[InputRequired(), Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 3...'})

    #question_2 = StringField('question_2', validators=[Length(min=4,max=120)], render_kw={'placeholder': 'Question 2...'}, default=None)
    #q2_answer = StringField('q2_answer', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'The right answer...'}, default=None)
    #q2_option_1 = StringField('q2_option_1', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 1...'}, default=None)
    #q2_option_2 = StringField('q2_option_2', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 2...'}, default=None)
    #q2_option_3 = StringField('q2_option_3', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 3...'}, default=None)

    # question_3 = StringField('question_3', validators=[Length(min=4,max=120)], render_kw={'placeholder': 'Question 3...'}, default=None)
    # q3_answer = StringField('q3_answer', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'The right answer...'}, default=None)
    # q3_option_1 = StringField('q3_option_1', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 1...'}, default=None)
    # q3_option_2 = StringField('q3_option_2', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 2...'}, default=None)
    # q3_option_3 = StringField('q3_option_3', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 3...'}, default=None)

    # question_4 = StringField('question_4', validators=[Length(min=4,max=120)], render_kw={'placeholder': 'Question 4...'}, default=None)
    # q4_answer = StringField('q4_answer', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'The right answer...'}, default=None)
    # q4_option_1 = StringField('q4_option_1', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 1...'}, default=None)
    # q4_option_2 = StringField('q4_option_2', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 2...'}, default=None)
    # q4_option_3 = StringField('q4_option_3', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 3...'}, default=None)

    # question_5 = StringField('question_5', validators=[Length(min=4,max=120)], render_kw={'placeholder': 'Question 5...'}, default=None)
    # q5_answer = StringField('q5_answer', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'The right answer...'}, default=None)
    # q5_option_1 = StringField('q5_option_1', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 1...'}, default=None)
    # q5_option_2 = StringField('q5_option_2', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 2...'}, default=None)
    # q5_option_3 = StringField('q5_option_3', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 3...'}, default=None)

    # question_6 = StringField('question_6', validators=[Length(min=4,max=120)], render_kw={'placeholder': 'Question 6...'}, default=None)
    # q6_answer = StringField('q6_answer', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'The right answer...'}, default=None)
    # q6_option_1 = StringField('q6_option_1', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 1...'}, default=None)
    # q6_option_2 = StringField('q6_option_2', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 2...'}, default=None)
    # q6_option_3 = StringField('q6_option_3', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 3...'}, default=None)

    # question_7 = StringField('question_7', validators=[Length(min=4,max=120)], render_kw={'placeholder': 'Question 7...'}, default=None)
    # q7_answer = StringField('q7_answer', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'The right answer...'}, default=None)
    # q7_option_1 = StringField('q7_option_1', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 1...'}, default=None)
    # q7_option_2 = StringField('q7_option_2', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 2...'}, default=None)
    # q7_option_3 = StringField('q7_option_3', validators=[Length(min=4,max=50)], render_kw={'placeholder': 'Wrong option 3...'}, default=None)
