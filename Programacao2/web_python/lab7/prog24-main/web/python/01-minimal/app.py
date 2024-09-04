from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/soma")
def soma():
    return str(8+10)

'''

execution (terminal):
$ flask run

if you want make the program available at network:
$ flask run --host=0.0.0.0

'''