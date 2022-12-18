"""
Form for answering quiz
"""

from flask_wtf import FlaskForm

class AnswerForm(FlaskForm):
    """
    Form for answering quiz
    """
    def __init__(self, questions): # pylint: disable=W0231
        self.questions = questions
        self.rigth_answers = []
        self.new_questions = []
        for question in self.questions:
            self.rigth_answers.append([question.id,question.answer])
            self.new_questions.append(([question.id, question.question],
                [question.answer, question.option_1, question.option_2, question.option_3]))
