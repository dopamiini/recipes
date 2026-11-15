""" Main application module. """
import secrets
import sqlite3
from flask import (
    Flask,
    abort,
    redirect,
    render_template,
    request,
    session,
)
import config
import users

app = Flask(__name__)
app.secret_key = config.SECRET_KEY


def require_login():
    """Checks user is logged in before allowing access a route."""
    if "user_id" not in session:
        abort(403)


def check_csrf():
    """Checks form submission has matching security token with the user's session."""
    if request.form.get("csrf_token") != session.get("csrf_token"):
        abort(403)


def get_flash_messages():
    """Flash messages stored in session for error and confirmation messages."""
    message = session.pop("message", None)
    message_type = session.pop("message_type", None)

    return message, message_type


@app.route("/")
def index():
    """Display the main page."""
    message, message_type = get_flash_messages()

    return render_template(
        "index.html",
        message=message,
        message_type=message_type,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    """Displays and processes the login form for the application."""
    if request.method == "GET":
        message, message_type = get_flash_messages()
        username = session.pop("login_username", "")

        return render_template(
            "login.html",
            message=message,
            message_type=message_type,
            username=username,
        )

    username = request.form["username"].strip()
    password = request.form["password"]

    if not username or not password:
        session["message"] = "Username and password are required."
        session["message_type"] = "error"
        session["login_username"] = username
        return redirect("/login")

    user = users.check_login(username, password)

    if user:
        session.pop("login_username", None)
        session["user_id"] = user["id"]
        session["username"] = username
        session["csrf_token"] = secrets.token_hex(16)
        return redirect("/")

    session["message"] = "Incorrect username or password!"
    session["message_type"] = "error"
    session["login_username"] = username
    return redirect("/login")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    """Logs out user and clears their login session information."""

    if request.method == "GET":
        return redirect("/")

    require_login()
    check_csrf()

    session.clear()

    return redirect("/")


@app.route("/register")
def register():
    """Displays the registration page."""
    message, message_type = get_flash_messages()
    username = session.pop("register_username", "")

    return render_template(
        "register.html", 
        message=message,
        message_type=message_type,
        username=username,
    )


@app.route("/create", methods=["POST"])
def create():
    """Processes the registered information and handles account creation."""
    username = request.form["username"].strip()
    password1 = request.form["password1"]
    password2 = request.form["password2"]

    if not username:
        message = "Username is required."
        session.pop("register_username", None)

    elif users.get_user_username(username):
        message = "Username already exists!"

    elif not password1:
        message = "Password is required!"

    elif not password2:
        message = "Please confirm your password!"

    elif password1 != password2:
        message = "Passwords are not the same!"

    else:
        message = None

    if message:
        session["message"] = message
        session["message_type"] = "error"

        if username:
            session["register_username"] = username

        return redirect("/register")

    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        session["message"] = "Username is already taken!"
        session["message_type"] = "error"
        return redirect("/register")

    session["message"] = "Account has been created successfully!"
    session["message_type"] = "success"
    return redirect("/")
