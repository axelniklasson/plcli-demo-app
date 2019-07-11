from flask import Flask
import logging
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello World from instance {os.getenv('PLCLI_INSTANCE_ID', -1)}"
