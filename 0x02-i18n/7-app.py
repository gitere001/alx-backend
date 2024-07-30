#!/usr/bin/env python3
'''Task: Define get_timezone function with timezone validation.

This module sets up a Flask application with Babel to handle
localization and timezone selection. It includes user retrieval,
timezone selection, and routing for the main page.
'''

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError


class Config:
    '''Configuration class for the Flask app.

    This class contains configuration settings for the Flask
    application, including debug mode, supported languages,
    default locale, and default timezone.
    '''
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    TIMEZONES = ["UTC", "Europe/Paris", "US/Central", "Asia/Kolkata"]


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieve a user based on a user id.

    Retrieves a user dictionary from the users list based on
    the `login_as` query parameter.

    Returns:
        dict or None: The user dictionary if found, None otherwise.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Perform routines before each request's resolution.

    Sets the global user object to the user retrieved from
    the `get_user` function.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Select and return the best language match based on supported languages.
    """
    # Locale from URL parameters
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc

    # Locale from user settings
    if g.user:
        loc = g.user.get('locale')
        if loc and loc in app.config['LANGUAGES']:
            return loc

    # Locale from request headers
    loc = request.headers.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc

    # Default to the best match from the request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Select and return the appropriate timezone.

    The order of priority is:
    1. Timezone from URL parameters
    2. Timezone from user settings
    3. Default to UTC
    """
    # Timezone from URL parameters
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except UnknownTimeZoneError:
            pass

    # Timezone from user settings
    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except UnknownTimeZoneError:
            pass

    # Default to UTC
    dflt = app.config['BABEL_DEFAULT_TIMEZONE']
    return dflt


@app.route('/')
def index() -> str:
    '''Render the homepage.

    Renders the homepage template.

    Returns:
        str: The rendered homepage template.
    '''
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
