#!/usr/bin/env python3
"""
Basic Flask app
"""


from flask import Flask, render_template


app: Flask = Flask(__name__)


def index() -> str:
    """Returns a string"""
    return render_template('0-index.html')


@app.route('/', strict_slashes=False)
def index_route() -> str:
    '''Return index'''
    return index()


if __name__ == '__main__':
    app.run()
