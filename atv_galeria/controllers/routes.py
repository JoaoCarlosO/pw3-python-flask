from flask import render_template, request, redirect, flash, current_app, url_for
from models.database import db, Imagem
from app import app
import os
import uuid

FILE_TYPES = {'png', 'jpg', 'jpeg', 'gif'}

def arquivos_permitidos(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES

@app.route('/')
def index():
    return redirect(url_for('galeria'))

@app.route('/galeria', methods=['GET', 'POST'])
def galeria():
    imagens = Imagem.query.all()

    if request.method == 'POST':
        file = request.files['file']

        if not arquivos_permitidos(file.filename):
            flash("Utilize os tipos de arquivos referentes a imagem.", 'danger')
            return redirect(request.url)

        file_extension = os.path.splitext(file.filename)[1]
        filename = str(uuid.uuid4()) + file_extension

        img = Imagem(filename=filename)
        db.session.add(img)
        db.session.commit()

        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        flash("Imagem enviada com sucesso!", 'success')
        return redirect(request.url)

    return render_template('galeria.html', imagens=imagens)
