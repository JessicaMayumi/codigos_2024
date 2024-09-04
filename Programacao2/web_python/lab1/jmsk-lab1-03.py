from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/soma")
def soma():
    # receber os números
    a = int(request.args.get('n1'))
    b = int(request.args.get('n2'))
    # retornar a soma
    return str(a+b)

