#!/usr/bin/python3
"""
Defines a script that listens on 0.0.0.0, port 5000 and displays provided
content.
"""

from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_dbs(exception):
    """Closes the storage on teardown"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML page with the states sorted by names"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
