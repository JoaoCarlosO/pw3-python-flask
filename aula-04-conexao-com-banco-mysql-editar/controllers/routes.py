from flask import render_template, request, redirect, url_for
from models.database import Game, db

# Lista de jogadores
jogadores = ['Miguel José', 'Miguel Isack', 'Leaf',
             'Quemario', 'Trop', 'Aspax', 'maxxdiego']

# Array de objetos - Lista de games
gamelist = [{'Título': 'CS-GO',
            'Ano': 2012,
             'Categoria': 'FPS Online'}]


def init_app(app):
    # Criando a primeira rota do site
    @app.route('/')
    # Criando função no Python
    def home():
        return render_template('index.html')

    # Rota de games
    @app.route('/games', methods=['GET', 'POST'])
    def games():
        game = gamelist[0]
        # Tratando se a requisição for do tipo POST
        if request.method == 'POST':
            # Verificar se o campo 'jogador' existe
            if request.form.get('jogador'):
                # O append adiciona o item a lista
                jogadores.append(request.form.get('jogador'))
            return redirect(url_for('games'))

        jogos = ['Jogo 1', 'Jogo 2', 'Jogo 3', 'Jogo 4', 'Jogo 5', 'Jogo 6']
        return render_template('games.html',
                               game=game,
                               jogadores=jogadores,
                               jogos=jogos)

    # Rota de cadastro de jogos (em dicionário)
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título': request.form.get('titulo'), 'Ano': request.form.get(
                    'ano'), 'Categoria': request.form.get('categoria')})
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               gamelist=gamelist)

    # Rota Crud (Estoque de jogos)
    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/<int:id>')
    def estoque(id=None):
        # se o Id for passado, então é para excluir o jogo
        if id:
            # Deletando o jogo do banco
            game = Game.query.get(id)
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque'))
        if request.method == 'POST':
            # Cadastro de jogos no banco
            newGame = Game(request.form.get('titulo'),
                           request.form.get('ano'),
                           request.form.get('categoria'), request.form.get('plataforma'), request.form.get('preco'))
            # Adicionando o jogo no banco
            db.session.add(newGame)
            db.session.commit()
            return redirect(url_for('estoque'))
        # ORM que estamos usnado é o SQLAlchemy
        # O método query.all = SELECT * FROM games
        gamesEmEstoque = Game.query.all()
        return render_template('estoque.html', gamesEmEstoque=gamesEmEstoque)

    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit(id):
        game = Game.query.get(id)
        if request.method == 'POST':
            game.titulo = request.form['titulo']
            game.ano = request.form['ano']
            game.categoria = request.form['categoria']
            game.plataforma = request.form['plataforma']
            game.preco = request.form['preco']
            db.session.commit()
            return redirect(url_for('estoque'))
        return render_template('editgame.html', game=game)
