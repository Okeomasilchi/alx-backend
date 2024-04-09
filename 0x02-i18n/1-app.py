#!/usr/bin/env python3
"""
Basic Babel setup
"""


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """Returns a string"""
    return render_template(
        '1-index.html',
        title='Welcome to Holberton',
        text='Hello world'
    )


if __name__ == '__main__':
    app.run()
