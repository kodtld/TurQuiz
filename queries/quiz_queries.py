from db import db

def add_quiz(subject, private, creator_id):
    sql = ("INSERT INTO Quizs (subject, private, creator_id) VALUES (:subject, :private, :creator_id)")
    db.session.execute(sql, {"subject": subject, "private": private, "creator_id":creator_id})
    db.session.commit()

def get_created_quiz(subject):
    sql = ("SELECT * FROM Quizs WHERE subject=:subject")
    result = db.session.execute(sql,{"subject": subject})
    return result.fetchone()

def add_question(question, answer, option_1, option_2, option_3, quiz_id):
    sql = ("INSERT INTO Questions (question, answer, option_1, option_2, option_3, quiz_id) VALUES (:question, :answer, :option_1, :option_2, :option_3, :quiz_id)")
    db.session.execute(sql, {"question": question, "answer": answer, "option_1": option_1, "option_2": option_2, "option_3": option_3, "quiz_id": quiz_id})
    db.session.commit()

def get_questions(quiz_id):
    sql = ("SELECT * FROM Questions WHERE quiz_id=:quiz_id")
    result = db.session.execute(sql, {"quiz_id": quiz_id})
    return result.fetchall()

def get_user_quizzes(creator_id):
    sql = ("SELECT * FROM Quizs WHERE creator_id=:creator_id ORDER BY id DESC")
    result = db.session.execute(sql, {"creator_id": creator_id})
    return result.fetchall()

def get_community_quizzes():
    sql = ("SELECT * FROM Quizs WHERE private=:private ORDER BY id DESC")
    result = db.session.execute(sql, {"private": "f"})
    return result.fetchall()

def delete_quiz(user_id,quiz_id):
    check = ("SELECT creator_id FROM Quizs WHERE id=:quiz_id")
    result = db.session.execute(check, {"quiz_id":quiz_id})
    if result.fetchone()[0] == user_id:
        sql = ("DELETE FROM Questions WHERE quiz_id=:quiz_id; DELETE FROM quizs WHERE id=:quiz_id")
        db.session.execute(sql,{"quiz_id":quiz_id, "id":quiz_id})
        db.session.commit()

def delete_empty_quiz(quiz_id):
    sql = ("DELETE FROM Quizs WHERE id=:quiz_id")
    db.session.execute(sql,{"quiz_id":quiz_id})
    db.session.commit()