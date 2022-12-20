# run program: python -m flask run, filename must be: app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World from Flask"