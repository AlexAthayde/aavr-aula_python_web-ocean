from flask import Flask

app = Flask('Meu App')

@app.route          ('/')
def hello():
    return "Hello Word"

@app.route          ('/novo')
def novo():
    return "<h1>Nova Página</h1>"
