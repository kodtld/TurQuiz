from app import app
from db import db, Users, Quizs, Questions
from flask_login import login_user, login_required, logout_user, current_user
from flask import render_template, redirect, session, request, url_for, flash

from random import choice, shuffle

from models.color import colors, title_colors
from models.quote import quotes

from forms.loginform import LoginForm
from forms.registerform import RegisterForm
from forms.create_quiz import QuizForm
from forms.create_questions import QuestionForm
from forms.answerform import AnswerForm

from werkzeug.security import generate_password_hash, check_password_hash


from compare_answers import compare_answers

from threads import add_user, add_quiz, get_created_quiz, add_question, get_questions, get_user_quizzes, get_community_quizzes

@app.route("/")
def index():
        color = choice(colors)
        title_color = title_colors[0]
        quote = choice(quotes)

        return render_template('home.html', color = color.code, title_color = title_color.code, quote=quote.content, author=quote.author)

@app.route("/register", methods=['GET', 'POST'])
def register():
        color = choice(colors)
        title_color = title_colors[0]
        
        form = RegisterForm()
        if form.validate_on_submit():
                hashed_password = generate_password_hash(form.password.data, method='sha256')
                add_user(form.username.data,form.email.data,hashed_password)
                flash("User created succesfully")

        return render_template('register.html', color = color.code, title_color = title_color.code, form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
        color = choice(colors)
        title_color = title_colors[0]

        form = LoginForm()
        if form.validate_on_submit():
                user = Users.query.filter_by(username=form.username.data).first()
                if user:
                        if check_password_hash(user.password, form.password.data):
                                login_user(user, remember=True)
                                return redirect(url_for('dash'))
                flash("Invalid username or password")
        return render_template('login.html', color = color.code, title_color = title_color.code, form = form)

@app.route('/logout')
@login_required
def logout():
        logout_user()
        return redirect(url_for('index'))

@app.route("/dash")
@login_required
def dash():
        color = choice(colors)
        title_color = title_colors[0]

        return render_template('dash.html', color = color.code, title_color = title_color.code, username = current_user.username)

@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
        color = choice(colors)
        title_color = title_colors[0]
        
        form = QuizForm()
        if form.validate_on_submit():
                add_quiz(form.subject.data, form.private.data, current_user.id)
                created_quiz = get_created_quiz(form.subject.data)

                return redirect(url_for('questions', subject=form.subject.data, subject_id=created_quiz.id))
        return render_template('new.html', color = color.code, title_color = title_color.code, form = form)

@app.route('/<subject>/<subject_id>/questions', methods=['GET', 'POST'])
@login_required
def questions(subject,subject_id):
        color = choice(colors)
        title_color = title_colors[0]

        form = QuestionForm()

        if form.validate_on_submit():
                add_question(form.question_1.data, form.q1_answer.data, form.q1_option_1.data, form.q1_option_2.data, form.q1_option_3.data, subject_id)
                return redirect(url_for('questions', subject=subject, subject_id=subject_id))

        return render_template('questions.html', color = color.code, title_color = title_color.code, form = form, subject=subject, subject_id = subject_id)

@app.route('/<subject>/<subject_id>/answer', methods=['GET', 'POST'])
@login_required
def answer(subject, subject_id):
        color = choice(colors)
        title_color = title_colors[0]

        checknumber = 0
        
        questions = get_questions(subject_id)
        form = AnswerForm(questions)
        right_answers = form.rigth_answers
        
        for question in form.new_questions:
                shuffle(question[1])

                if request.method == 'POST' and checknumber == 0:
                        checknumber +=1
                        score = compare_answers(right_answers, request.values)
                        print(score, "%")
                

        return render_template('answers.html', color = color.code, title_color = title_color.code, form = form.new_questions, subject = subject, subject_id = subject_id)

@app.route('/my_quizzes')
@login_required
def my_quizzes():
        color = choice(colors)
        title_color = title_colors[0]

        quizzes = get_user_quizzes(current_user.id)
        return render_template('my_quizzes.html', color = color.code, title_color = title_color.code, quizzes = quizzes)


@app.route('/community_quizzes')
@login_required
def community_quizzes():
        color = choice(colors)
        title_color = title_colors[0]

        quizzes = get_community_quizzes()
        return render_template('community_quizzes.html', color = color.code, title_color = title_color.code, quizzes = quizzes)
