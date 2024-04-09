#!/usr/bin/env python3
"""
Use user locale
"""


from flask import Flask, render_template, g, request
from flask_babel import Babel, gettext


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
    """Get user from mock database"""
    return users.get(user_id, None)


app: Flask = Flask(__name__)
babel: Babel = Babel(app)


class Config:
    """Config class for Babel"""
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


@app.before_request
def before_request() -> None:
    """Set user globally in flask.g"""
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None


@app.route('/')
def index():
    """Render index template"""
    return render_template(
        '5-index.html',
        title=gettext('home_title'),
        header=gettext('home_header')
    )


if __name__ == '__main__':
    app.run()
