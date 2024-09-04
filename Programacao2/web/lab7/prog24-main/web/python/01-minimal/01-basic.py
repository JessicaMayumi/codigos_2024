'''
pré-requisito: é preciso instalar a biblioteca Flask

use um destes comandos abaixo no terminal:

$ python3 -m pip install flask
OU
$ pip3 install flask

referências:
https://packaging.python.org/en/latest/tutorials/installing-packages/
https://flask.palletsprojects.com/en/3.0.x/installation/#install-flask

Caso seja necessário atualizar o pip:

$ python3 -m pip install --upgrade pip
OU
$ pip3 install --upgrade pip

obs: no windows (em sua casa), quando for instalar o python,
marque a opção "Add Python X.X to PATH":
https://youtu.be/K027HB-_PIw?t=118

'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()

'''
how to execute:

1a) open the program in Visual Studio Code and "play" it

OR

1b) run on terminal:

$ python3 01-basic.py

3) for "using" it, on web browser call:

http://localhost:5000

OR

http://127.0.0.1:5000

'''