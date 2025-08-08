from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils import db, lm  # db = SQLAlchemy(), lm = LoginManager()
from controllers.usuario import bp_usuarios  # Blueprint de rotas relacionadas a usuários
from controllers.mensagem import bp_mensagem  # Blueprint de rotas relacionadas a mensagens
from models.usuario import Usuario  # Modelo de dados para o usuário
from models.mensagem import mensagem  # Modelo de dados para mensagens (possivelmente deveria ser "Mensagem")

app = Flask(__name__)

# Configurações da aplicação
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Caminho do banco de dados SQLite
app.config['SECRET_KEY'] = 'PIZZA'  # Chave secreta usada para sessões e segurança
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa alertas desnecessários do SQLAlchemy

# Inicialização das extensões com o app Flask
db.init_app(app)  # Inicializa o banco de dados
lm.init_app(app)  # Inicializa o gerenciador de login
migrate = Migrate(app, db)  # Configura migrações com Flask-Migrate

# Registro dos blueprints (rotas separadas em arquivos diferentes)
app.register_blueprint(bp_usuarios, url_prefix='/user')  # Rotas de usuário
app.register_blueprint(bp_mensagem, url_prefix='/mensagem')  # Rotas de mensagem

# ----------------------------- ROTAS PRINCIPAIS -----------------------------

# Página inicial (capa do site)
@app.route('/')
def capa():
    return render_template('capa.html')

# Página de criação de usuário
@app.route('/usuario_create')
def usuario_create():
    return render_template('usuario_create.html')

# Página "Sobre", com informações do projeto ou da equipe
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Página de contatos (e-mail, redes sociais, etc.)
@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

# Página principal após login ou acesso ao sistema
@app.route('/principal')
def principal():
    return render_template('principal.html')

# Página de abertura de chamados (reclamações, sugestões, etc.)
@app.route('/abrirchamado')
def abrirchamado():
    return render_template('abrir_chamados.html')
