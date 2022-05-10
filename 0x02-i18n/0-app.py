#!/usr/bin/env python3

"""
    Initial setup of a basic Flask app
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ route to render the index page """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
