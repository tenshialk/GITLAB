from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils import db,lm
from models.mensagem import mensagem    
from flask_login import login_user, logout_user
from flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

bp_usuarios = Blueprint("mensagem", __name__, template_folder='templates')

