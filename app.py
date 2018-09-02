#!/usr/bin/python3
"""APP"""
from classes import storage
from classes.url_class import URL
from flask import abort, Flask, jsonify, redirect, request, render_template
import random
import requests
import string


app = Flask(__name__)
#app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.url_map.strict_slashes = False


def random_string():
    """generate a random string for short_url"""
    return "".join(random.choice(string.ascii_letters) for i in range(6))


@app.errorhandler(404)
def not_found(error):
    """return custom 404 page
       return render_template("custom_404.html")
    """
    pass


@app.route('/', methods=['GET'])
def index():
    """return landing page with search bar form accepting long url"""
    return render_template("index.html")


@app.route('/', methods=['POST'])
def create_short_url():
    """return generated short url in response to form submission"""
    user_input = request.form["URL"]
    long_url = user_input
    short_url = ""
    try:
        if long_url and not long_url.startswith("http"):
            long_url = "https://" + long_url
        if long_url:
            short_url = random_string()
            attributes = {"short_url": short_url, "long_url": long_url}
            obj = URL(**attributes)
            storage.save(obj)
    except:
        pass
    return render_template("index.html",
                           long_url=long_url,
                           short_url=short_url)


@app.route('/<short_url>', methods=['GET'])
def go_to_short_url(short_url):
    """return original url page"""
    try:
        original_url = storage.get(short_url)
        return redirect(original_url)
    except:
        abort(400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
