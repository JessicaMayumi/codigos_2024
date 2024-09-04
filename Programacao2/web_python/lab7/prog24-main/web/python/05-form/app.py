from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "System ok"

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/sum")
def sum():
    # receive the numbers
    a = int(request.args.get('n1'))
    b = int(request.args.get('n2'))
    sum = a + b
    return f'A soma é: {sum}'

'''
reference:
https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates

run:
$ flask run
'''