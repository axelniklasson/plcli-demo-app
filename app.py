from flask import Flask
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
