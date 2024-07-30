#!/usr/bin/env python3
""" a Flask route decorator that handles the root URL ("/") and renders the"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """Configuration class for Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Create Flask app instance
app = Flask(__name__)

# Load configuration from Config class
app.config.from_object(Config)

# Initialize Babel with the Flask app
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """
    A Flask route decorator that handles the root URL ("/") and renders the
    "1-index.html" template.

    Returns:
        The rendered HTML content of the "1-index.html" template.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
