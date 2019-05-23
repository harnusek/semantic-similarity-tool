#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main module of the server file
"""

from flask import render_template
import connexion
import logging
from logging.handlers import RotatingFileHandler

# Create the application instance
server = connexion.App(__name__, specification_dir="./")

# Read the swagger.yml file to configure the endpoints
server.add_api("swagger.yml")


# create a URL route in our application for "/"
@server.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


if __name__ == "__main__":
    # handler = RotatingFileHandler('logs.log', maxBytes=10000, backupCount=1)
    # handler.setLevel(logging.INFO)
    # app.app.logger.addHandler(handler)
    server.run(debug=True)
