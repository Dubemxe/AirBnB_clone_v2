#!/usr/bin/python3
"""
Defines a script that listens on 0.0.0.0, port 5000 and displays 'Hello HBNB'
And on another route - /hbnb displays 'HBNB'
On a new route - /c/<text> displays 'C' followed by the content of '<text>'
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
    """Dispalys C followed by the content of <text>"""
    if text == "_":
        return " "
    return f"C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
