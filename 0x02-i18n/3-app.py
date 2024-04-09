#!/usr/bin/env python3
"""
Get locale from request
"""


from flask import Flask, render_template, request
from flask_babel import Babel, gettext


def get_locale() -> str:
    """Get locale from request"""
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
        )


app: Flask = Flask(__name__)
babel: Babel = Babel(app, locale_selector=get_locale)


# @babel.localeselector



class Config:
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index_route() -> str:
    """Returns a string"""
    return render_template(
      '3-index.html',
      title=gettext('home_title'),
      header=gettext('home_header')
      )


if __name__ == '__main__':
    app.run()
