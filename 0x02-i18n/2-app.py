#!/usr/bin/env python3
"""
Get locale from request
"""


from flask import Flask, render_template, request
from flask_babel import Babel


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
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
        )


def index() -> str:
    """Returns a string"""
    return render_template('1-index.html')


@app.route('/', strict_slashes=False)
def index_route() -> str:
    '''Return index'''
    return index()


if __name__ == '__main__':
    app.run()
