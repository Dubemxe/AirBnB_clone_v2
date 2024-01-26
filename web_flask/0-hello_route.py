#!/usr/bin/python3
"""
Defines a script that listens on 0.0.0.0, port 5000 and displays 'Hello HBNB'
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
	"""Dispalys Hello HBNB!"""
	return "Hello HBNB!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000')
