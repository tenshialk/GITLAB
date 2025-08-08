from utils import db

class mensagem(db.Model):
    __tablename__= "mensagem"
    id = db.Column(db.Integer, primary_key = True)
    matricula = db.Column(db.String(100))

    def __init__(self, matricula):
        self.matricula = matricula
    
    def __repr__(self):
        return "<Usuario {}>".format(self.matricula)