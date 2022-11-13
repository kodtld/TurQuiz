from flask import Flask
from flask import render_template, redirect, url_for
from random import choice
from models.color import colors, title_colors
from models.quote import quotes
from forms.loginform import LoginForm
from forms.registerform import RegisterForm
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