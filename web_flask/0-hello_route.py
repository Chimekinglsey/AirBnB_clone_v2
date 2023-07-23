#!/usr/bin/python3
"""
0. Hello Flask!
This module creates a simple flask application that listens at 0.0.0.0 port 5000
for all connections. By default, flask runs on port 5000. if not, the app.run
	will look like: app.run(host='0.0.0.0', port=5000)
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
	"""This method prints greeting to School"""
	return "Hello HBNB!"


if __name__ == '__main__':
	app.run(host='0.0.0.0')
