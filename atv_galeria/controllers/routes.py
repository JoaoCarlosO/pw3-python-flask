from flask import render_template, request, redirect, flash, current_app
from models.database import db, Imagem
import os
import uuid

# Definindo tipos de arquivos permitidos
FILE_TYPES = set(['png', 'jpg', 'jpeg', 'gif'])

def arquivos_permitidos(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES

def galeria():
    # Seleciona os nomes dos arquivos de imagens no banco
    imagens = Imagem.query.all()
    
    if request.method == 'POST':
        # Captura o arquivo vindo do formulário
        file = request.files['file']
        
        # Verifica se a extensão do arquivo é permitida
        if not arquivos_permitidos(file.filename):
            flash("Utilize os tipos de arquivos referentes a imagem.", 'danger')
            return redirect(request.url)
        
        # Define um nome aleatório para o arquivo
        file_extension = os.path.splitext(file.filename)[1]
        filename = str(uuid.uuid4()) + file_extension
        
        # Gravando o nome do arquivo no banco
        img = Imagem(filename=filename)
        db.session.add(img)
        db.session.commit()
        
        # Salva o arquivo na pasta de uploads
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        
        flash("Imagem enviada com sucesso!", 'success')
        return redirect(request.url)
        
    return render_template('galeria.html', imagens=imagens)