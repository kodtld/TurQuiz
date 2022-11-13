from flask import Flask
from flask import render_template
from random import choice
from models.color import colors, title_colors
from models.quote import quotes
from forms.loginform import LoginForm
from forms.registerform import RegisterForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdrtghj65w4525'

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
                return '<h1>' + form.username.data + ' ' + form.password.data + form.email.data +'</h1>'

        return render_template('register.html', color = color.code, title_color = title_color.code, form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
        color = choice(colors)
        title_color = title_colors[0]

        form = LoginForm()
        if form.validate_on_submit():
                return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'


        return render_template('login.html', color = color.code, title_color = title_color.code, form = form)
