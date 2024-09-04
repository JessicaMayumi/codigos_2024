from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "System ok"

@app.route("/sum")
def soma():
    # receive the numbers
    a = int(request.args.get('n1'))
    b = int(request.args.get('n2'))
    sum = a + b
    # deliver the sum to the page
    return render_template("sum.html", total = sum)

'''
reference:
https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates

run:
$ flask run
'''