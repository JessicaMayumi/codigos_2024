#9 - É preciso armazenar 4 informações sobre carros (modelo, cor, placa e ano) em um banco de dados. 
#Forneça a definição de uma classe persistente em python que realize essa demanda; utilize o framework pony.

from flask import Flask, render_template, request, redirect
from pony.orm import *

db = Database()
app = Flask(__name__)

class Carro(db.Entity):
    modelo = Required(str)
    cor = Required(str)
    placa = Required(str)
    ano = Required(str)
    
    def __str__(self):
        return f"{self.modelo}, {self.cor}, {self.placa}, {self.dono}"
    
db.bind(provider="sqlite", filename="carros.db", create_db=True)
db.generate_mapping(create_tables=True)

with db_session:
    carro = Carro(modelo="a", cor="b", placa="c", ano="d")

    commit()

    #teste
    print(carro.modelo, carro.cor, carro.placa, carro.ano)
    