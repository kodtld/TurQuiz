from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_login import LoginManager, UserMixin

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")#.replace("://", "ql://", 1)

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

class Highscores(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        quiz_id = db.Column(db.Integer)
        user_id = db.Column(db.Integer)
        score = db.Column(db.Integer)

class Answerank(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer)
        amount = db.Column(db.Integer)
        level = db.Column(db.String(50))

class Createrank(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer)
        level = db.Column(db.String(50))


@login_manager.user_loader
def load_user(user_id):
        return Users.query.get(int(user_id))