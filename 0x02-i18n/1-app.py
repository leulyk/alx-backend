#!/usr/bin/env python3

"""
    Babel test 0
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ class that acts as a template for language configuration """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """ route to render the index page """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
