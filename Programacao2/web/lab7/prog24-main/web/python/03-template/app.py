from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "System ok"

@app.route("/about")
def about():
    return render_template("about.html")

'''
reference:
https://flask.palletsprojects.com/en/3.0.x/quickstart/#rendering-templates

run:
$ flask run
'''