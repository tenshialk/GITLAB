from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def capa():
    return render_template('capa.html')

@app.route('/usuario_create')
def usuario_create():
    return render_template('usuario_create.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/principal')
def principal():
    return render_template('principal.html')

@app.route('/abrirchamado')
def abrirchamado():
    return render_template('abrir chamados.html')