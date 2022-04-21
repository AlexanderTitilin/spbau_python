#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import flask
from flask import Flask, request


def caesar(message, step):
    return "".join([chr(ord(s) + step) for s in message])


app = Flask(__name__, template_folder="templates")


@app.route("/")
def root():
    return flask.render_template("root.html")


@app.route("/encrypt", methods=["POST", "GET"])
def encrypt():
    text = request.form.get('message') 
    step = request.form.get('step')
    result = ""
    if not step is None:
        result = caesar(text,int(step))
    return flask.render_template("encrypt.html",caesar=result)


@app.route("/decrypt", methods=["POST", "GET"])
def decrypt():
    text = request.form.get('message') 
    step = request.form.get('step')
    result = ""
    if not step  is None:
       result = caesar(text,-int(step))
    return flask.render_template("decrypt.html",caesar=result)


if __name__ == "__main__":
    app.run(debug=True)
