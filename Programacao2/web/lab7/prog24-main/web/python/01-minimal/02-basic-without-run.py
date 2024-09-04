from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

'''

for execution, open terminal in the folder where 
the program is located and run:
$ flask --app 02-basic-without-run run

reference:
# https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application

if you want make the program available at network:
$ flask --app 02-basic-without-run run --host=0.0.0.0

'''