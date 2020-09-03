#!/usr/bin/python3
"""Module that starts a Flask web application
    """
from flask import Flask, render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def display_text_integer(n):
    """Method that returns n is a number
    if n is a integer

    Args:
        n ([int]): Integer to return

    Returns:
        [str]: n is a number
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_template(n):
    """Method that returns with a number

    Args:
        n ([int]): integer to render on the template

    Returns:
        [html]: html with the integer in the paramether
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
