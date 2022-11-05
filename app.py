from flask import Flask
from flask import render_template
from random import choice
from models.color import Color
from models.quote import Quote
app = Flask(__name__)

@app.route("/")
def index():
        colors = [Color("Mauvelous","#EB98A5","light"),Color("Dark Orange","#FFA033","light"),
                Color("Lilac", "#C6A4CC","light"),Color("Pink Lavender", "#E0B1CB","light")]
        color = choice(colors)
        title_colors = [Color("Dark Cyan","#2A8D88","dark"), Color("Medium Turquoise","#52CBC5","light")]
        title_color = title_colors[0]

        quotes = [Quote("It is what we know already that often prevents us from learning.","Claude Bernard"),
                Quote("Tell me and I forget. Teach me and I remember. Involve me and I learn.","Benjamin Franklin"),
                Quote("Question everything. Learn something. Answer nothing.","Euripides"),
                Quote("I am always ready to learn although I do not always like being taught.","Winston Churchill"),
                Quote("The first problem for all of us, men and women, is not to learn, but to unlearn.","Gloria Steinem"),
                Quote("I am always doing that which I cannot do, in order that I may learn how to do it.","Pablo Picasso")]
        quote = choice(quotes)

        return render_template('home.html', color = color.code, title_color = title_color.code, quote=quote.content, author=quote.author)

@app.route("/register")
def register():
        colors = [Color("Mauvelous","#EB98A5","light"),Color("Dark Orange","#FFA033","light"),
                Color("Lilac", "#C6A4CC","light"),Color("Pink Lavender", "#E0B1CB","light")]
        color = choice(colors)
        
        title_colors = [Color("Dark Cyan","#2A8D88","dark"), Color("Medium Turquoise","#52CBC5","light")]
        title_color = title_colors[0]
        return render_template('register.html', color = color.code, title_color = title_color.code)

@app.route("/login")
def login():
        colors = [Color("Mauvelous","#EB98A5","light"),Color("Dark Orange","#FFA033","light"),
                Color("Lilac", "#C6A4CC","light"),Color("Pink Lavender", "#E0B1CB","light")]
        color = choice(colors)
        
        title_colors = [Color("Dark Cyan","#2A8D88","dark"), Color("Medium Turquoise","#52CBC5","light")]
        title_color = title_colors[0]

        return render_template('login.html', color = color.code, title_color = title_color.code)
