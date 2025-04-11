from flask_sqlalchemy import SQLAlchemy

# Carregando o SQLAlchemy em uma variável
db = SQLAlchemy()

# Classe entidade Games
class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titluo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    paltaforma = db.Column(db.String(150))
    preco = db.Column(db.Float)
    descricao = db.Column(db.Text)
    
    # método construtor da classe

    def __init__(self, titluo, ano, categoria, paltaforma, preco, descricao):
        self.titluo = titluo
        self.ano = ano
        self.categoria = categoria
        self.paltaforma = paltaforma
        self.preco = preco
        self.descricao = descricao
        return f'<Games {self.titluo}>'