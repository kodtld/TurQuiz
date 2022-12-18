from db import db

def add_user(username, email, password):
    sql = ("INSERT INTO Users (username, email, password) VALUES (:username, :email, :password)")
    db.session.execute(sql, {"username": username, "email": email, "password":password})
    db.session.commit()

def get_user(username):
    sql = ("SELECT * FROM Users WHERE username = :username")
    result = db.session.execute(sql, {"username": username})
    return result.fetchone()