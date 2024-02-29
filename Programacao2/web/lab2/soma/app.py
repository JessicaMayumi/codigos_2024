from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/form")
def index():
    return render_template("index.html")

@app.route("/sum")
def sum():
    a = int(request.args.get('num1'))
    b = int(request.args.get('num2'))
    sum = a + b
    return f'A soma é: {sum}'


