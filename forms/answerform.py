from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, RadioField
from wtforms.validators import InputRequired, Length

class AnswerForm(FlaskForm):
    def __init__(self, questions):
        self.questions = questions
        self.rigth_answers = []
        self.new_questions = []
        for question in self.questions:
            self.rigth_answers.append([question.id,question.answer])
            self.new_questions.append(([question.id, question.question],[question.answer, question.option_1, question.option_2, question.option_3]))

    

