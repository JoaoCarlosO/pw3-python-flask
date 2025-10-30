from flask import render_template, request, url_for, redirect, flash
from models.database import db, Imagem
import os
import uuid

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    
    # Definindo tipos de arquivos permitidos
    FILE_TYPES = set(['png', 'jpg', 'jpeg', 'gif'])
    
    def arquivos_permitidos(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES
        
    # UPLOAD DE IMAGENS
    @app.route('/galeria', methods=['GET', 'POST'])
    def galeria():
        # Seleciona os nomes dos arquivos de imagens no banco
        imagens = Imagem.query.all()
        
        if request.method == 'POST':
            file = request.files['file']
            # Verifica se o tipo de arquivo é permitido
            if not arquivos_permitidos(file.filename):
                flash("Utilize os tipos de arquivos referentes a imagem.", 'danger')
                return redirect(request.url)
            
            # Criando um nome aleatório para o arquivo
            filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
            
            # Gravando o nome do arquivo no banco
            img = Imagem(filename)
            db.session.add(img)
            db.session.commit()
            
            # Gravando o arquivo na pasta de uploads
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("Imagem enviada com sucesso!", 'success')
            return redirect(url_for('galeria'))
            
        return render_template('galeria.html', imagens=imagens)

    # Rota para deletar imagens
    @app.route('/galeria/delete/<int:id>')
    def delete_image(id):
        imagem = Imagem.query.get(id)
        if imagem:
            # Remove o arquivo físico
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], imagem.filename)
            if os.path.exists(file_path):
                os.remove(file_path)
            
            # Remove do banco de dados
            db.session.delete(imagem)
            db.session.commit()
            flash("Imagem deletada com sucesso!", 'success')
        
        return redirect(url_for('galeria'))