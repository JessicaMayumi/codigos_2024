from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/table")
def tabela():
    return render_template("table.html")

'''
reference:
https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates

run:
$ flask run
'''