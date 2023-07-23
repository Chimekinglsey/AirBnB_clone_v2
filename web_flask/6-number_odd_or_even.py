#!/usr/bin/python3
"""
This module creates a simple flask application that listens at 0.0.0.0 port
5000 for all connections. By default, flask runs on port 5000. if not,
the app.run will look like: app.run(host='0.0.0.0', port=5000)
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
    """This method prints greeting to School"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This prints `HBNB` for all root/hbnb requests"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
    """This prints `C` plus text received for all root/c/<text> requests"""
    if text:
        text = text.replace("_", " ")
        return f"C {text}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Displays Python followed by the text passed"""
    if text != "is cool":
        text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def int_num(n):
    """Displays passed number only if it's a number"""
    """if type(n) == int:
        return f"{n} is a number"
    else:
        pass"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """displays a HTML page only if `n` is an integer"""
    return render_template('5-number.html', value=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """evaluates if an `int` is divisible by 2 or not"""
    if n % 2 == 0:
        num = f"{n} is even"
        return render_template("6-number_odd_or_even.html", value=num)
    else:
        num = f"{n} is odd"
        return render_template("6-number_odd_or_even.html", value=num)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
