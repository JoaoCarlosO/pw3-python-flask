from flask import Flask
from models.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///imagens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'minha-chave-secreta'

db.init_app(app)

# Importar e registrar as rotas
from controllers.routes import galeria
app.add_url_rule('/galeria', 'galeria', galeria, methods=['GET', 'POST'])

@app.route('/')
def index():
    from flask import redirect, url_for
    return redirect(url_for('galeria'))

if __name__ == '__main__':
    import os
    with app.app_context():
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        db.create_all()
    app.run(debug=True)