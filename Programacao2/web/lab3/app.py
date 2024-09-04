from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/form")
def index():
    return render_template("index.html")

@app.route("/raiz")
def raiz():
    a = int(request.args.get('num1'))
    b = int(request.args.get('num2'))
    c = int(request.args.get('num3'))
    delta = (b*b) - 4*a*c
    if delta < 0:
        return render_template("resultado.html", resultado = "Não existe raíz!")
    elif delta == 0:
        total = -b/(2*a)
        return render_template("resultado.html", resultado = f"Raíz: {total}")
    else:
        total1 = (-b + math.sqrt(delta))/(2*a)
        total2 = (-b + math.sqrt(delta))/(2*a)
        return render_template("resultado.html", resultado = f"Raíz 1: {total1}\tRaíz 2: {total2}")
    


