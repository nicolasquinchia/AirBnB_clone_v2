#!/usr/bin/python3
"""
Experimenting with flask
"""
from flask import Flask, render_template
from models import storage, State, Amenity
app = Flask(__name__)


@app.teardown_appcontext
def ripandtear(_):
    """Rips and tears
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """Filters
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    lili = [states, amenities]
    return render_template('10-hbnb_filters.html', pair=lili)

if __name__ == '__main__':
    storage.reload()
    app.run('0.0.0.0', 5000)