''' TBl Plantao'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plantao(db.Model):
    __tablename__ = 'plantoes'
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    horario_inicio = db.Column(db.Time, nullable=False)
    horario_fim = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='disponível')
    recorrencia = db.Column(db.String(20), nullable=True)  # definir depois
    
    def __repr__(self):
        return f"<Plantao {self.id} - {self.data} ({self.horario_inicio}-{self.horario_fim})>"
