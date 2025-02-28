from flask import render_template, request

jogadores = ['iruh', 'davi_lambari', 'edsongf',
             'kioto', 'black butterfly', 'jujudopix']


def init_app(app):
    # Criando a rota principal do site
    @app.route('/')
    # Criando função no Python
    # View function - Função de vizualização
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        # Dicionário no Python(obejto)
        game = {'Título': 'CS-GO',
                'Ano': 2012,
                'Categoria': 'FPS Online'}

        if request.method == 'POST':
            if request.form.get('jogador'):  # name da input
                jogadores.append(request.form.get('jogador'))

        jogos = ['Fortnite', 'League of Legends', 'CrossFire', 'Roblox',
                 'PUBG', 'Minecraft', 'Lost Ark', 'Counter-Strike: Global Offensive']

        return render_template('games.html', game=game, jogadores=jogadores, jogos=jogos)
