#config 1°

from flask import Flask, render_template, request, redirect
from pony.orm import *

db = Database()
app = Flask(__name__)

#model 2°

class Pessoa(db.Entity):
    nome = Required(str)
    email = Required(str)
    telefone = Required(str) # ou 
    
    def __str__(self):
        return f"{self.nome}, {self.email}, {self.telefone}"
    
db.bind(provider="sqlite", filename="person.db", create_db=True)
db.generate_mapping(create_tables=True)

#app.py 3° - em caso de arquivos separados dar importe dos outros 2 arquivos

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/listar/<str:classe>")
def listar(classe):
    with db_session:
        if classe == "pessoa":
            pessoas = Pessoa.select()
            return render_template("listar.html", pessoas=pessoas)
        elif classe == "filme":
            r=r #aleatorio pq nao terminou o codigo
            #outra classe

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/adicionar_pessoa")
def adicionar_pessoa():
    #passo 1 - pegar os parâmetros, quando a rota for chamada
    nome = request.args.get("nome") 
    email = request.args.get("email")
    telefone = request.args.get("telefone")

    with db_session: #passo 2 - abrir seção para manipular o banco de dados
        p = Pessoa (**request.args) # "**" associa os elemntos do dicionário aos elementos do objeto
        commit() #confirma a alteração
        return redirect("listar") #resposta da alteração
