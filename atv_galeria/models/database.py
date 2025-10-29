from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Imagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
