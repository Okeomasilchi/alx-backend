#!/usr/bin/env python3
"""
Force locale with URL parameter
"""


from flask import Flask, render_template, request
from flask_babel import Babel, gettext


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
    """Get locale from request"""
    f = request.args.get('locale')
    ret = request.accept_languages.best_match(app.config['LANGUAGES'])
    return f if f and f in app.config['LANGUAGES'] else ret


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
