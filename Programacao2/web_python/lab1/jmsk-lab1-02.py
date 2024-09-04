from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/soma")
def soma():
    return str(8+11)

@app.route("/multi")
def multi():
    return str(5*3)