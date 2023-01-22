#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /:Displays 'Hello HBNB!'
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "c {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays  'is a number" preceded by value of <n>."""
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML page with H1: "Number: n" inside BODY."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays a HTML page with H1: "Number: n is even|odd" inside BODY."""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
