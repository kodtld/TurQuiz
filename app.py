from flask import Flask
from flask import render_template, redirect, url_for
from random import choice
from models.color import colors, title_colors
from models.quote import quotes
from forms.loginform import LoginForm
from forms.registerform import RegisterForm
from forms.create_quiz import QuizForm
from forms.create_questions import QuestionForm
from forms.answerform import AnswerForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdrtghj65w4525'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///kxsalmi"
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class Users(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(15), unique=True)
        email = db.Column(db.String(50), unique=True)
        password = db.Column(db.String(80))
        
class Quizs(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        subject = db.Column(db.String(25), unique=True)
        private = db.Column(db.Boolean)
        creator_id = db.Column(db.Integer)

class Questions(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        question = db.Column(db.String(120))
        answer = db.Column(db.String(50))
        option_1 = db.Column(db.String(50))
        option_2 = db.Column(db.String(50))
        option_3 = db.Column(db.String(50))
        quiz_id = db.Column(db.Integer)

@login_manager.user_loader
def load_user(user_id):
        return Users.query.get(int(user_id))

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
                new_user = Users(username=form.username.data, email=form.email.data,password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                return '<h1>New user created!</h1>'
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
                return '<h1>Invalid credentials :(</h1>'
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
                new_quiz = Quizs(subject=form.subject.data,private=form.private.data,creator_id=current_user.id)
                db.session.add(new_quiz)
                db.session.commit()
                created_quiz = Quizs.query.filter_by(subject=form.subject.data).first()

                return redirect(url_for('questions', subject=form.subject.data, subject_id=created_quiz.id))
        return render_template('new.html', color = color.code, title_color = title_color.code, form = form)

@app.route('/<subject>/<subject_id>/questions', methods=['GET', 'POST'])
@login_required
def questions(subject,subject_id):
        color = choice(colors)
        title_color = title_colors[0]

        form = QuestionForm()

        if form.validate_on_submit():
                new_question = Questions(
                        question = form.question_1.data,
                        answer = form.q1_answer.data,
                        option_1 = form.q1_option_1.data,
                        option_2 = form.q1_option_2.data,
                        option_3 = form.q1_option_3.data,
                        quiz_id = subject_id
                )
                db.session.add(new_question)
                db.session.commit()
                return redirect(url_for('questions', subject=subject, subject_id=subject_id))

        return render_template('questions.html', color = color.code, title_color = title_color.code, form = form, subject=subject, subject_id = subject_id)

@app.route('/<subject>/<subject_id>/answer', methods=['GET', 'POST'])
@login_required
def answer(subject, subject_id):
        color = choice(colors)
        title_color = title_colors[0]

        questions = Questions.query.filter_by(quiz_id=subject_id)

        form = AnswerForm(questions)
        print(form.rigth_answers)
        print(form.new_questions)

        return render_template('answers.html', color = color.code, title_color = title_color.code, form = form.new_questions, subject = subject, subject_id = subject_id)

@app.route('/my_quizzes')
@login_required
def my_quizzes():
        color = choice(colors)
        title_color = title_colors[0]

        quizzes = Quizs.query.filter_by(creator_id=current_user.id).order_by(-Quizs.id)
        return render_template('my_quizzes.html', color = color.code, title_color = title_color.code, quizzes = quizzes)


@app.route('/community_quizzes')
@login_required
def community_quizzes():
        color = choice(colors)
        title_color = title_colors[0]

        quizzes = Quizs.query.filter_by(private="f").order_by(-Quizs.id)
        return render_template('community_quizzes.html', color = color.code, title_color = title_color.code, quizzes = quizzes)

