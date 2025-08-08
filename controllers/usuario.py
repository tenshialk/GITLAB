from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils import db,lm
from models.usuario import Usuario
from flask_login import login_user, logout_user
from flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

bp_usuarios = Blueprint("usuarios", __name__, template_folder='templates')

@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('Cadastro.html')
    
    if request.method == 'POST':
        matricula = request.form.get('matricula')
        email = request.form.get('matricula')
        senha = request.form.get('senha')
        senha_criptografada = generate_password_hash(senha)

        if len(senha) < 3:
            flash('A senha precisa de pelo menos 3 caracteres.')
            return redirect(url_for('usuarios.create'))

        if Usuario.query.filter_by(email=email).first():
            flash('matricula já cadastrado!')
            return redirect(url_for('usuarios.create'))

        if Usuario.query.filter_by(matricula=matricula).first():
            flash('Matrícula já cadastrada!')
            return redirect(url_for('usuarios.create'))

        usuario = Usuario(matricula=matricula, senha=senha_criptografada)
        db.session.add(usuario)
        db.session.commit()

        login_user(usuario)
        return redirect(url_for('principal'))