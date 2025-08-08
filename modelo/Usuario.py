from utils import db

class Usuario(db.Model):
    __tablename__= "usuario"
    id = db.Column(db.Integer, primary_key = True)
    matricula = db.Column(db.String(100))
    senha = db.Column(db.String(100))

    def __init__(self, matricula, senha):
        self.matricula = matricula
        self.senha = senha
    
    def __repr__(self):
        return "<Usuario {}>".format(self.matricula)