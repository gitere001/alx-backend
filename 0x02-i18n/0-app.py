#!/usr/bin/env python3
""" a Flask route decorator that handles the root URL (/) and renders the"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    A Flask route decorator that handles the root URL ("/") and renders the
    "0-index.html" template.

    Returns:
        The rendered HTML content of the "0-index.html" template.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
