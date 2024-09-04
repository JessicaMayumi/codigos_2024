#11 - Forneça um código python flask que receba os parâmetros enviados na seguinte requisição http: 

#http://localhost:5000/soma?n1=5&n2=10


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/form")
def index():
    return render_template("index.html")

@app.route("/soma")
def soma():
    a = int(request.args.get('n1'))
    b = int(request.args.get('n2'))
    sum = a + b
    return f'A soma é: {soma}'


