#!/usr/bin/env python3

"""
    i18n project: task 2
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ class that acts as a template for language configuration """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """ route to render the index page """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """ determines the best match with our supported languages """
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.run()
