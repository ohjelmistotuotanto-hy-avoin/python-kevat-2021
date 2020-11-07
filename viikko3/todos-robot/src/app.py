from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    session,
    flash
)

from user_repository import user_repository
from todo_repository import todo_repository
from user import User
from todo import Todo

app = Flask(__name__)
app.secret_key = "MXRg2upmZGaSR~2nMaGmiwW0o.lg_w"


def redirect_to_login():
    return redirect(url_for("render_login"))


def redirect_to_todos():
    return redirect(url_for("render_todos"))


def redirect_to_register():
    return redirect(url_for("render_register"))


def get_current_user():
    if "username" in session:
        return user_repository.find_by_username(session["username"])

    return None


@app.route("/")
def render_home():
    current_user = get_current_user()

    if current_user:
        return redirect_to_todos()

    return redirect_to_login()


@app.route("/login", methods=["GET"])
def render_login():
    current_user = get_current_user()

    if current_user:
        return redirect_to_todos()

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def handle_login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        flash("Username and password are required")
        return redirect_to_login()

    user = user_repository.find_by_username(username)

    if not user or user.password != password:
        flash("Invalid username or password")
        return redirect_to_login()

    session["username"] = user.username

    flash(f"Welcome back {user.username}!")

    return redirect_to_todos()


@app.route("/logout", methods=["POST"])
def logout():
    del session["username"]
    return redirect_to_login()


@app.route("/register", methods=["GET"])
def render_register():
    current_user = get_current_user()

    if current_user:
        return redirect_to_todos()

    return render_template("register.html")


@app.route("/register", methods=["POST"])
def handle_register():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        flash("Username and password are required")
        return redirect_to_register()

    existing_user = user_repository.find_by_username(username)

    if existing_user:
        flash(f"Username already exists")
        return redirect_to_register()

    user_repository.create(User(username, password))
    session["username"] = username

    return redirect_to_todos()


@app.route("/todos", methods=["GET"])
def render_todos():
    current_user = get_current_user()

    if not current_user:
        return redirect_to_login()

    todos = todo_repository.find_by_username(current_user.username)

    return render_template("todos.html", todos=todos, todos_count=len(todos), user=current_user)


@app.route("/todos", methods=["POST"])
def create_todo():
    current_user = get_current_user()

    if not current_user:
        return redirect_to_login()

    content = request.form.get("content")

    if not content:
        flash("Content is required")
        return redirect_to_todos()

    todo_repository.create(Todo(content, user=current_user))

    return redirect_to_todos()


@app.route("/todos/<todo_id>/delete", methods=["POST"])
def delete_todo(todo_id):
    current_user = get_current_user()

    if not current_user:
        return redirect_to_login()

    todo = todo_repository.find_by_id(todo_id)

    if not todo or not todo.user or todo.user.username != current_user.username:
        return redirect_to_todos()

    todo_repository.delete(todo_id)

    return redirect_to_todos()

# tämän avulla voi tarkastaa onko palvelin käynnissä
@app.route("/ping")
def ping():
    return "pong"

# sovelluksen tilan alustaminen testejä varten
@app.route("/tests/reset")
def reset_tests():
    if "username" in session:
        del session["username"]

    user_repository.delete_all()
    todo_repository.delete_all()

    # luodaan yksi testikäyttäjä
    user_repository.create(User('johndoe', 'secret'))

    return redirect_to_login()
