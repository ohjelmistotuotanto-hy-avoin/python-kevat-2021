from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request
)

from counter import Counter

app = Flask(__name__)
counter = Counter()


def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None


def redirect_to_counter():
    return redirect(url_for("render_counter"))


@app.route("/")
def render_counter():
    return render_template("counter.html", value=counter.value)


@app.route("/increase", methods=["POST"])
def increase():
    counter.increase()
    return redirect_to_counter()


@app.route("/decrease", methods=["POST"])
def decrease():
    counter.decrease()
    return redirect_to_counter()


@app.route("/reset", methods=["POST"])
def reset():
    counter.reset()
    return redirect_to_counter()


@app.route("/set-value", methods=["POST"])
def set_value():
    value = request.form.get("value")
    int_value = safe_int(value)

    if int_value:
        counter.value = int_value

    return redirect_to_counter()

# tämän avulla voi tarkastaa onko palvelin käynnissä
@app.route("/ping")
def ping():
    return "pong"

# sovelluksen tilan alustaminen testejä varten
@app.route("/tests/reset")
def reset_tests():
    counter.reset()
    return redirect_to_counter()
