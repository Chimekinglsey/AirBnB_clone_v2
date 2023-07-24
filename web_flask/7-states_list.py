#!/usr/bin/python3
"""
the app.run will look like: app.run(host='0.0.0.0', port=5000)
"""

from flask import Flask, render_template
from models import storage, State


app = Flask(__name__)


@app.teardown_appcontext
def rm_session(exception=None):
    """Tear_down method,removes current session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """lists the states"""
    states = "States"
    s_list = list(storage.all(State).values)
    return render_template('7-states_list.html', value=states,
                           state_list=s_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
