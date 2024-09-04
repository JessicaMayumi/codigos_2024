# https://flask.palletsprojects.com/en/3.0.x/quickstart/#variable-rules

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/soma/<int:n1>/<int:n2>")
def soma(n1, n2):
    a = int(n1)
    b = int(n2)
    # retornar a soma
    return f'A soma é: <h2>{a+b}</h2>'

'''

program execution:
$ flask --app app2 run

access on web browser:
localhost:5000/soma/5/10

'''