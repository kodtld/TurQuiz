from db import db

def add_user(username, email, password):
    sql = ("INSERT INTO Users (username, email, password) VALUES (:username, :email, :password)")
    db.session.execute(sql, {"username": username, "email": email, "password":password})
    db.session.commit()

def get_user(username):
    sql = ("SELECT * FROM Users WHERE username = :username")
    result = db.session.execute(sql, {"username": username})
    return result.fetchone()

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

def get_highscores(user_id):
    sql = ("SELECT q.id, q.subject, q.private, q.creator_id, h.score FROM Quizs AS q JOIN Highscores AS h ON h.user_id=:user_id AND q.id=h.quiz_id WHERE private=:private ORDER BY id DESC")
    result = db.session.execute(sql, {"private":"f", "user_id":user_id})
    return result.fetchall()

def delete_quiz(user_id,quiz_id):
    check = ("SELECT creator_id FROM Quizs WHERE id=:quiz_id")
    result = db.session.execute(check, {"quiz_id":quiz_id})
    if result.fetchone()[0] == user_id:
        sql = ("DELETE FROM Questions WHERE quiz_id=:quiz_id; DELETE FROM quizs WHERE id=:quiz_id")
        db.session.execute(sql,{"quiz_id":quiz_id, "id":quiz_id})
        db.session.commit()

def save_highscore(quiz_id, user_id, score):
    current_high = ("SELECT Score FROM highscores WHERE quiz_id=:quiz_id AND user_id=:user_id")

    result = db.session.execute(current_high, {"quiz_id": quiz_id, "user_id": user_id})
    result = result.fetchone()
    
    if result == None:
        new_high = ("INSERT INTO Highscores (quiz_id, user_id, score) VALUES (:quiz_id, :user_id, :score)")
        db.session.execute(new_high, {"quiz_id": quiz_id, "user_id": user_id, "score": score})
        db.session.commit()

    elif result != None:
        result = result[0]
        if result < score:
            new_high = ("UPDATE Highscores SET score=:score WHERE quiz_id=:quiz_id AND user_id=:user_id")
            db.session.execute(new_high, {"quiz_id": quiz_id, "user_id": user_id, "score": score})
            db.session.commit()

def add_answerank(user_id):
    sql = ("INSERT INTO Answerank (user_id, amount, level) VALUES (:user_id, :amount, :level)")
    db.session.execute(sql, {"user_id": user_id, "amount":0, "level":"Bronze"})
    db.session.commit()
    
def add_createrank(user_id):
    sql = ("INSERT INTO Createrank (user_id, level) VALUES (:user_id, :level)")
    db.session.execute(sql, {"user_id": user_id, "level":"Bronze"})
    db.session.commit()

def get_answerank(user_id):
    sql = ("SELECT amount, level FROM Answerank WHERE user_id=:user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    return result.fetchone()

def get_createrank(user_id):
    sql = ("SELECT subject FROM quizs WHERE creator_id=:user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    
    level = ("SELECT level FROM Createrank WHERE user_id=:user_id")
    level = db.session.execute(level, {"user_id": user_id})
    
    return len(result.fetchall()), level.fetchone()[0]

def update_answerank_amount(user_id):
        amnt = get_answerank(user_id)[0]
        amnt += 1
        new_rank = ("UPDATE Answerank SET amount=:amount WHERE user_id=:user_id")
        db.session.execute(new_rank, {"amount":amnt,"user_id": user_id})
        db.session.commit()

def update_answerank_level(user_id, level):
        new_rank = ("UPDATE Answerank SET level=:level WHERE user_id=:user_id")
        db.session.execute(new_rank, {"level":level,"user_id": user_id})
        db.session.commit()

def update_createrank(user_id, level):
        new_rank = ("UPDATE Createrank SET level=:level WHERE user_id=:user_id")
        db.session.execute(new_rank, {"level": level, "user_id": user_id})
        db.session.commit()