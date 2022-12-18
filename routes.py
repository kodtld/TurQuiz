"""
Routes module
Controls the url routes, and functions, services, etc. called by them
"""
from random import choice, shuffle
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask import render_template, redirect, request, url_for, flash


from app import app
from db import Users

from models.color import colors, title_colors
from models.quote import quotes

from forms.loginform import LoginForm
from forms.registerform import RegisterForm
from forms.create_quiz import QuizForm
from forms.create_questions import QuestionForm
from forms.answerform import AnswerForm

from services import rankservice, answerservice

from queries.user_queries import add_user, get_user
from queries.quiz_queries import (add_quiz, get_created_quiz, add_question, get_questions,
    get_user_quizzes, get_community_quizzes, delete_quiz, delete_empty_quiz)

from queries.highscore_queries import get_highscores, save_highscore
from queries.rank_queries import add_answerank, add_createrank, update_answerank_amount

@app.route("/")
def index():
    """
    Home page
    """
    color = choice(colors)
    title_color = title_colors[0]
    quote = choice(quotes)

    return render_template('home.html', color = color.code, title_color = title_color.code,
        quote=quote.content, author=quote.author)

@app.route("/register", methods=['GET', 'POST'])
def register():
    """
    Register user page
    If created user is valid and unique, creates user and inputs to db
    """
    color = choice(colors)
    title_color = title_colors[0]

    form = RegisterForm()
    if form.validate_on_submit():
        try:
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            add_user(form.username.data,form.email.data,hashed_password)
            created_user = get_user(form.username.data)
            add_answerank(created_user.id)
            add_createrank(created_user.id)
            flash("User created succesfully!")

        except:
            flash("Username or email already in use!")

    if request.method == "POST" and not form.validate_on_submit():
        flash("Please enter valid values!")

    return render_template('register.html', color = color.code, title_color = title_color.code,
        form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Login page
    If user exists, logs the user in
    """
    color = choice(colors)
    title_color = title_colors[0]

    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=True)
                return redirect(url_for('dash'))
        flash("Invalid username or password!")
    return render_template('login.html', color = color.code, title_color = title_color.code,
        form = form)

@app.route('/logout')
@login_required
def logout():
    """
    Logs the "current_user" out
    """
    logout_user()
    return redirect(url_for('index'))

@app.route("/dash")
@login_required
def dash():
    """
    Dashboard page
    Includes links to community, and user created quizzes
    """
    color = choice(colors)
    title_color = title_colors[0]

    return render_template('dash.html', color = color.code, title_color = title_color.code,
        username = current_user.username)

@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    """
    New quiz page
    If created quiz is valid and unique, imports to db
    """
    color = choice(colors)
    title_color = title_colors[0]

    form = QuizForm()
    try:
        if form.validate_on_submit():
            add_quiz(form.subject.data, form.private.data, current_user.id)
            created_quiz = get_created_quiz(form.subject.data)

            return redirect(url_for('questions', subject=form.subject.data,
            subject_id=created_quiz.id))

    except:
        flash("A quiz by the same name already exists!")

    return render_template('new.html', color = color.code, title_color = title_color.code,
        form = form)

@app.route('/<subject>/<subject_id>/questions', methods=['GET', 'POST'])
@login_required
def questions(subject,subject_id):
    """
    Add questions for created quiz page
    """
    color = choice(colors)
    title_color = title_colors[0]

    form = QuestionForm()

    if form.validate_on_submit():
        add_question(form.question_1.data, form.q1_answer.data, form.q1_option_1.data,
            form.q1_option_2.data, form.q1_option_3.data, subject_id)

        return redirect(url_for('questions', subject=subject, subject_id=subject_id))

    return render_template('questions.html', color = color.code, title_color = title_color.code,
        form = form, subject=subject, subject_id = subject_id)

@app.route('/<subject>/<subject_id>/answer', methods=['GET', 'POST'])
@login_required
def answer(subject, subject_id):
    """
    Answer selected quiz
    If all questions answered, redirects to user score page
    """
    color = choice(colors)
    title_color = title_colors[0]

    checknumber = 0
    got_questions = get_questions(subject_id)

    if len(got_questions) == 0:
        delete_empty_quiz(subject_id)
        return render_template('empty.html', color = color.code, title_color = title_color.code)

    form = AnswerForm(got_questions)
    right_answers = form.rigth_answers

    for question in form.new_questions:
        shuffle(question[1])

        if request.method == 'POST' and checknumber == 0:
            if len(request.values) == len(right_answers):
                checknumber +=1
                score = answerservice.compare_answers(right_answers, request.values)
                score = (int(score) * 777)
                update_answerank_amount(current_user.id)
                return redirect(url_for('myscore', subject=subject, subject_id=subject_id,
                    score=score))

            checknumber +=1
            flash("Please answer all the questions!")


    return render_template('answers.html', color = color.code, title_color = title_color.code,
        form = form.new_questions, subject = subject, subject_id = subject_id)

@app.route('/<subject>/<subject_id>/<score>/myscore')
@login_required
def myscore(subject, subject_id, score):
    """
    Shows user score for answered quiz
    If highscore, saves the highscore to db
    """
    score = (int(score) / 777)
    color = choice(colors)
    title_color = title_colors[0]

    save_highscore(subject_id, current_user.id, score)

    return render_template('score.html', color = color.code, title_color = title_color.code,
        subject = subject, score = score)

@app.route('/my_quizzes')
@login_required
def my_quizzes():
    """
    My quizzes page
    Show all quizzes created by logged in user
    """
    color = choice(colors)
    title_color = title_colors[0]

    quizzes = get_user_quizzes(current_user.id)
    return render_template('my_quizzes.html', color = color.code, title_color = title_color.code,
        quizzes = quizzes)

@app.route('/community_quizzes')
@login_required
def community_quizzes():
    """
    Community quizzes page
    Shows all public quizzes from all users
    """
    color = choice(colors)
    title_color = title_colors[0]

    quizzes = get_community_quizzes()
    return render_template('community_quizzes.html', color = color.code,
        title_color = title_color.code, quizzes = quizzes)

@app.route('/my_scores')
@login_required
def my_scores():
    """
    My scores page
    Shows user highscores and user ranks
    """
    color = choice(colors)
    title_color = title_colors[0]

    quiz_and_score = get_highscores(current_user.id)
    ranks = rankservice.get_ranks(current_user.id)

    answer_rankcolor_code = rankservice.get_rankcolor(ranks[1])
    create_rankcolor_code = rankservice.get_rankcolor(ranks[3])

    return render_template('my_scores.html', color = color.code, title_color = title_color.code,
        quiz_and_score = quiz_and_score, answer_rankcolor_code = answer_rankcolor_code.code,
        create_rankcolor_code = create_rankcolor_code.code, ranks = ranks)

@app.route('/<subject_id>/delete', methods=['GET'])
@login_required
def delete(subject_id):
    """
    Deletes selected quiz, if logged in user == creator
    """
    delete_quiz(current_user.id,subject_id)
    return redirect(url_for('my_quizzes'))
