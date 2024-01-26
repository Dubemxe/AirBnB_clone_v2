#!/usr/bin/python3
"""
Defines a script that listens on 0.0.0.0, port 5000 and displays provided
content.
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    """Dispalys Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Dispalys HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    """Displays C followed by the content of <text>"""
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text='is cool'):
    """Displays Python followed by the content of <text>"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """display n is a number only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_templates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def display_number_eo(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        value = 'even'
    else:
        value = 'odd'
    return render_template('6-number_odd_or_even.html', value=value, n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
