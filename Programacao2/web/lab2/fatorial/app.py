from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return "OIHHHHHH"

@app.route("/form")
def index():
    return render_template("index.html")

@app.route("/fat")
def fat():
    a = int(request.args.get('num1'))
    fat = 1
    for i in range(1,a+1):
        fat *= i
    return render_template("resultado.html", total = fat)

