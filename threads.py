from db import db

def add_user(username, email, password):
    sql = ("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)")
    db.session.execute(sql, {"username": username, "email": email, "password":password})
    db.session.commit()

def add_quiz(subject, private, creator_id):
    sql = ("INSERT INTO quizs (subject, private, creator_id) VALUES (:subject, :private, :creator_id)")
    db.session.execute(sql, {"subject": subject, "private": private, "creator_id":creator_id})
    db.session.commit()

def get_created_quiz(subject):
    sql = ("SELECT * FROM quizs WHERE subject=:subject")
    result = db.session.execute(sql,{"subject": subject})
    return result.fetchone()

def add_question(question, answer, option1, option2, option3, quiz_id):
    sql = ("INSERT INTO questions (question, answer, option1, option2, option3, quiz_id) VALUES (:question, :answer, :option1, :option2, :option3, :quiz_id)")
    db.session.execute(sql, {"question": question, "answer": answer, "option1": option1, "option2": option2, "option3": option3, "quiz_id": quiz_id})
    db.session.commit()

def get_questions(quiz_id):
    sql = ("SELECT * FROM questions WHERE quiz_id=:quiz_id")
    result = db.session.execute(sql, {"quiz_id": quiz_id})
    return result.fetchall()

def get_user_quizzes(creator_id):
    sql = ("SELECT * FROM quizs WHERE creator_id=:creator_id ORDER BY id DESC")
    result = db.session.execute(sql, {"creator_id": creator_id})
    return result.fetchall()

def get_community_quizzes():
    sql = ("SELECT * FROM quizs WHERE private=:private ORDER BY id DESC")
    result = db.session.execute(sql, {"private": "f"})
    return result.fetchall()