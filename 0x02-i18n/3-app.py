#!/usr/bin/env python3
""" 3. Parametrize templates """

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ A config class to define """
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Get locale """
    return render_template("3-index.html")

if __name__ == "__main__":
    app.run()
