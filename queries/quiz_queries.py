"""
All queries controlling quiz actions
"""

from db import db

def add_quiz(subject, private, creator_id):
    """
    Query for creating a quiz
    """
    sql = ("INSERT INTO Quizs (subject, private, creator_id) VALUES (:subject, :private, :creator_id)")
    db.session.execute(sql, {"subject": subject, "private": private, "creator_id":creator_id})
    db.session.commit()

def get_created_quiz(subject):
    """
    Query for fetching just created quiz
    """
    sql = ("SELECT * FROM Quizs WHERE subject=:subject")
    result = db.session.execute(sql,{"subject": subject})
    return result.fetchone()

def add_question(question, answer, option_1, option_2, option_3, quiz_id): # pylint: disable=R0913
    """
    Query for adding a question to created quiz
    """
    sql = ("INSERT INTO Questions (question, answer, option_1, option_2, option_3, quiz_id) VALUES (:question, :answer, :option_1, :option_2, :option_3, :quiz_id)")
    db.session.execute(sql, {"question": question, "answer": answer, "option_1": option_1, "option_2": option_2, "option_3": option_3, "quiz_id": quiz_id})
    db.session.commit()

def get_questions(quiz_id):
    """
    Query for getting quiz specific questions
    """
    sql = ("SELECT * FROM Questions WHERE quiz_id=:quiz_id")
    result = db.session.execute(sql, {"quiz_id": quiz_id})
    return result.fetchall()

def get_user_quizzes(creator_id):
    """
    Query for getting all quizzes created by logged user
    """
    sql = ("SELECT * FROM Quizs WHERE creator_id=:creator_id ORDER BY id DESC")
    result = db.session.execute(sql, {"creator_id": creator_id})
    return result.fetchall()

def get_community_quizzes():
    """
    Query for getting all community created public quizzes
    """
    sql = ("SELECT * FROM Quizs WHERE private=:private ORDER BY id DESC")
    result = db.session.execute(sql, {"private": "f"})
    return result.fetchall()

def delete_quiz(user_id,quiz_id):
    """
    Query for deleting a quiz
    """
    check = ("SELECT creator_id FROM Quizs WHERE id=:quiz_id")
    result = db.session.execute(check, {"quiz_id":quiz_id})
    if result.fetchone()[0] == user_id:
        sql = ("DELETE FROM Questions WHERE quiz_id=:quiz_id; DELETE FROM quizs WHERE id=:quiz_id")
        db.session.execute(sql,{"quiz_id":quiz_id, "id":quiz_id})
        db.session.commit()

def delete_empty_quiz(quiz_id):
    """
    Query that deletes an empty quiz if answer is tried
    """
    sql = ("DELETE FROM Quizs WHERE id=:quiz_id")
    db.session.execute(sql,{"quiz_id":quiz_id})
    db.session.commit()
