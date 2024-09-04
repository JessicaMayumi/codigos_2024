#config 1°

from flask import Flask, render_template, request, redirect
from pony.orm import *

db = Database()
app = Flask(__name__)

#model 2°

class Gato(db.Entity):
    nomeAnimal = Required(str)
    genero = Required(str)
    nomeDono = Required(str) # ou Opcional
    raca = Required(str)
    cor = Required(str)
    doenca = Optional(str)
    
    def __str__(self):
        return f"{self.nomeAnimal}, {self.genero}, {self.nomeDono}, {self.raca}, {self.cor}, {self.doenca}"
    
db.bind(provider="sqlite", filename="gatos.db", create_db=True)
db.generate_mapping(create_tables=True)

#app.py 3° - em caso de arquivos separados dar importe dos outros 2 arquivos

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/listar")
def listar():
    with db_session:
        gatos = Gato.select()
        return render_template("listar.html", gatos=gatos)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/adicionar_pessoa")
def adicionar_pessoa():
    #passo 1 - pegar os parâmetros, quando a rota for chamada
    nomeAnimal = request.args.get("nomeAnimal") 
    genero = request.args.get("genero")
    nomeDono = request.args.get("nomeDono")
    raca = request.args.get("raca")
    cor = request.args.get("cor")
    doenca = request.args.get("doenca")


    with db_session: #passo 2 - abrir seção para manipular o banco de dados
        g = Gato (**request.args) # "**" associa os elemntos do dicionário aos elementos do objeto
        commit() #confirma a alteração
        return redirect("listar") #resposta da alteração
