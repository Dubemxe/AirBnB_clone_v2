#!/usr/bin/python3
"""
Defines a script that listens on 0.0.0.0, port 5000 and displays 'Hello HBNB'
And on another route - /hbnb displays 'HBNB'
On a new route - /c/<text> displays 'C' followed by the content of '<text>'
another route - /python and /python/<text> displays 'Python' followed by the content of '<text>'
or 'is cool' as default.
"""
from flask import Flask
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
def display_C(text='is cool'):
    """Displays Python followed by the content of <text>"""
    if text == "_":
        return " "
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
