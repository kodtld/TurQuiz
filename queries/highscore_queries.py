"""
Queries for higscores
"""
from db import db # pylint: disable=E0401

def get_highscores(user_id):
    """
    Gets user highscores by user_id
    """
    sql = ("SELECT q.id, q.subject, q.private, q.creator_id, h.score FROM Quizs AS q JOIN Highscores AS h ON h.user_id=:user_id AND q.id=h.quiz_id WHERE private=:private ORDER BY id DESC")
    result = db.session.execute(sql, {"private":"f", "user_id":user_id})
    return result.fetchall()

def save_highscore(quiz_id, user_id, score):
    """
    Saves user highscores
    """
    current_high = ("SELECT Score FROM highscores WHERE quiz_id=:quiz_id AND user_id=:user_id")

    result = db.session.execute(current_high, {"quiz_id": quiz_id, "user_id": user_id})
    result = result.fetchone()

    if result is None:
        new_high = ("INSERT INTO Highscores (quiz_id, user_id, score) VALUES (:quiz_id, :user_id, :score)")
        db.session.execute(new_high, {"quiz_id": quiz_id, "user_id": user_id, "score": score})
        db.session.commit()

    elif result is not None:
        result = result[0]
        if result < score:
            new_high = ("UPDATE Highscores SET score=:score WHERE quiz_id=:quiz_id AND user_id=:user_id")
            db.session.execute(new_high, {"quiz_id": quiz_id, "user_id": user_id, "score": score})
            db.session.commit()
