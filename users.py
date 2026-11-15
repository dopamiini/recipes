"""Database helpers for user management and authentication."""
from werkzeug.security import check_password_hash, generate_password_hash
import db


def get_user_username(username):
    """Helper function to check if registered user exists."""
    sql = "SELECT id, username FROM users WHERE username = ?"
    res = db.query(sql, [username])
    return res[0] if res else None


def create_user(username, password):
    """Tries to create a username with given password."""
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])


def check_login(username, password):
    """Checks if login credentials are valid. Used to validate user for /login."""
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    res = db.query(sql, [username])

    if len(res) != 1:
        return None

    if check_password_hash(res[0]["password_hash"], password):
        return res[0]

    return None
