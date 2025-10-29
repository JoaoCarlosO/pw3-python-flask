from flask import Flask
from models.database import db
import os

app = Flask(__name__, template_folder='views')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///imagens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'minha-chave-secreta'

db.init_app(app)

from controllers import routes

if __name__ == '__main__':
    with app.app_context():
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        db.create_all()
    app.run(debug=True)
