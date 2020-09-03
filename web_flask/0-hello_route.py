#!/usr/bin/python3
"""Module that starts a Flask web application
    """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Method that returns Hello test for a
    web server request
        [str]: Display "Hello HBNB!"
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
