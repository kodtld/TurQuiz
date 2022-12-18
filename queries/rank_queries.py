"""
Queries for answer rank and creator ranks
"""

from db import db

def add_answerank(user_id):
    """
    Inits answer rank for user
    """
    sql = ("INSERT INTO Answerank (user_id, amount, level) VALUES (:user_id, :amount, :level)")
    db.session.execute(sql, {"user_id": user_id, "amount":0, "level":"Bronze"})
    db.session.commit()

def add_createrank(user_id):
    """
    Inits create rank for user
    """
    sql = ("INSERT INTO Createrank (user_id, level) VALUES (:user_id, :level)")
    db.session.execute(sql, {"user_id": user_id, "level":"Bronze"})
    db.session.commit()

def get_answerank(user_id):
    """
    Fetches user answer rank
    """
    sql = ("SELECT amount, level FROM Answerank WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    return result.fetchone()

def get_createrank(user_id):
    """
    Fetches user creator rank
    """
    sql = ("SELECT subject FROM quizs WHERE creator_id=:user_id")
    result = db.session.execute(sql, {"user_id": user_id})

    level = ("SELECT level FROM Createrank WHERE user_id=:user_id")
    level = db.session.execute(level, {"user_id": user_id})

    return len(result.fetchall()), level.fetchone()[0]

def update_answerank_amount(user_id):
    """
    Updates the amount of answered quizzes for user
    """
    amnt = get_answerank(user_id)[0]
    amnt += 1
    new_rank = ("UPDATE Answerank SET amount=:amount WHERE user_id=:user_id")
    db.session.execute(new_rank, {"amount":amnt,"user_id": user_id})
    db.session.commit()

def update_answerank_level(user_id, level):
    """
    Updates the rank name to match corresponding amount value
    """
    new_rank = ("UPDATE Answerank SET level=:level WHERE user_id=:user_id")
    db.session.execute(new_rank, {"level":level,"user_id": user_id})
    db.session.commit()

def update_createrank(user_id, level):
    """
    Updates the rank name to match corresponding amount value
    """
    new_rank = ("UPDATE Createrank SET level=:level WHERE user_id=:user_id")
    db.session.execute(new_rank, {"level": level, "user_id": user_id})
    db.session.commit()
