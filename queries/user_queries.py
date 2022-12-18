"""
Queries for creating and fetching users
"""

from db import db

def add_user(username, email, password):
    """
    Query for creating an user
    """
    sql = ("INSERT INTO Users (username, email, password) VALUES (:username, :email, :password)")
    db.session.execute(sql, {"username": username, "email": email, "password":password})
    db.session.commit()

def get_user(username):
    """
    Query for fetching an user
    """
    sql = ("SELECT * FROM Users WHERE username = :username")
    result = db.session.execute(sql, {"username": username})
    return result.fetchone()
