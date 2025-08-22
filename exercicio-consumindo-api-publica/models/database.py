from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Classe responsável por criar a entidade "Console"
class Console(db.Model):
    __tablename__ = "consoles"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    fabricante = db.Column(db.String(150), nullable=False)
    ano_lancamento = db.Column(db.Integer, nullable=False)

    def __init__(self, nome, fabricante, ano_lancamento):
        self.nome = nome
        self.fabricante = fabricante
        self.ano_lancamento = ano_lancamento


# Classe responsável por criar a entidade "Musica"
class Musica(db.Model):
    __tablename__ = "musicas"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)

    def __init__(self, titulo, ano, categoria, preco, quantidade):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade
