from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils import db,lm
from models.usuario import Usuario
from flask_login import login_user, logout_user
from flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

bp_usuarios = Blueprint("usuarios", __name__, template_folder='templates')

@bp_usuarios.route('/usuario_create', methods=['GET', 'POST'])
def usuario_create():
    if request.method == 'GET':
        return render_template('usuario_create.html')
    if request.method == 'POST':
        matricula = request.form.get('matricula')
        senha = request.form.get('senha')
        if not matricula or not senha:
            flash('Preencha todos os campos.')
            return redirect(url_for('usuarios.login'))

        usuario = Usuario.query.filter_by(matricula=matricula).first()

        if not usuario:
            flash('Matrícula não encontrada.')
            return redirect(url_for('usuarios.login'))

        if not check_password_hash(usuario.senha, senha):
            flash('Senha incorreta.')
            return redirect(url_for('usuarios.login'))

        # Sucesso no login (pode usar session, Flask-Login, etc.)
        session['usuario_id'] = usuario.id
        flash(f'Bem-vindo(a), {usuario.nome}!')
        return redirect(url_for('principal'))  # Altere para a página pós-login

        


