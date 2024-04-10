#!/usr/bin/env python3
"""
Use user locale
"""


from flask import Flask, render_template, g, request
from flask_babel import Babel, gettext, format_datetime
from datetime import datetime
import pytz


users = {
    1: {
        "name": "Balou",
        "locale": "fr",
        "timezone": "Europe/Paris"
    },
    2: {
        "name": "Beyonce",
        "locale": "en",
        "timezone": "US/Central"
    },
    3: {
        "name": "Spock",
        "locale": "kg",
        "timezone": "Vulcan"
    },
    4: {
        "name": "Teletubby",
        "locale": None,
        "timezone": "Europe/London"
    },
}


def get_user(user_id: int) -> dict:
    """
    Retrieve a user from the users dictionary
    based on the given user_id.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict: The user information if found, None otherwise.
    """
    return users.get(user_id, None)


def validate_timezone(timezone: str) -> bool:
    """
    Validate if the timezone is valid.

    Args:
        timezone (str): The timezone to be validated.

    Returns:
        bool: True if the timezone is valid, False otherwise.
    """
    try:
        pytz.timezone(timezone)
        return True
    except pytz.exceptions.UnknownTimeZoneError:
        return False


app: Flask = Flask(__name__)
babel: Babel = Babel(app)


class Config:
    """
    Config class for Babel.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for Babel.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    Get locale based on user preference,
    URL parameters, or request headers
    """
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['LANGUAGES']:
        return url_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Get timezone based on user preference,
    URL parameters, or default to UTC
    """
    if g.user and g.user.get('timezone') and validate_timezone(
      g.user.get('timezone')
      ):
        return g.user.get('timezone')

    url_timezone = request.args.get('timezone')
    if url_timezone and validate_timezone(url_timezone):
        return url_timezone

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request() -> None:
    """Set user globally in flask.g.

    This function is executed before each request is
    processed by the Flask application. It retrieves
    the user ID from the request arguments and sets
    the user globally in the `flask.g` object.

    Args:
        None

    Returns:
        None
    """
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None


@app.route('/')
def index():
    """Render index template.

    This function renders the index template and
    passes the translated title and header to
    the template.

    Returns:
        The rendered index template.
    """
    return render_template(
        'index.html',
        title=gettext('home_title'),
        header=gettext('home_header'),
        time=format_datetime(datetime.now())
    )


if __name__ == '__main__':
    app.run()
