#!/usr/bin/python3
"""
 a script that starts a Flask web application:
    listening on 0.0.0.0, port 5000
    Routes:
        /: display Hello HBNB!
        /hbnb: display HBNB
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ display Hello HBNB!"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ display HBNB """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """
    display “C ” followed by the value
    of the text variable (replace
    underscore _ symbols with a space
    """
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False, defaults={"text": "is_cool"})
def hello_python(text="is_cool"):
    """display text for python """
    return("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def if_num_check(n):
    """display n is a number only if n is an integer """
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_num(n):
    """ html """
    return (render_template("5-number.html", n=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
