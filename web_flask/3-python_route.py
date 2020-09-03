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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Method that returns HBNB text test for a
    web server request
        [str]: Display HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text_C(text):
    """ Method that returns "C <text>
    Args:
        text ([str]): URL variable
    Returns:
        [str]: Display "C " followed by the value of the text variable
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_text_pythonic(text='is cool'):
    """Method that returns "Python <text>

    Args:
        text (str, optional): text after Python. Defaults to 'is cool'.

    Returns:
        [str]: Display "Python " followed by the value of the text variable
    """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
