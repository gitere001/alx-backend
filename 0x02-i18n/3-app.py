#!/usr/bin/env python3
"""Flask configuration and application setup."""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Configuration class for Flask and Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Returns the best matching locale from the list of available locales based
    on the user's accepted languages.
    This function is used as a localeselector for the Flask-Babel extension.

    :return: A string representing the best matching locale.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    A Flask route decorator that handles the root URL ("/") and renders the
    "3-index.html" template.

    Returns:
        The rendered HTML content of the "3-index.html" template.
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
