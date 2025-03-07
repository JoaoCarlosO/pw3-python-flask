from flask import render_template, request

jogadores = ['iruh', 'davi_lambari', 'edsongf',
             'kioto', 'black butterfly', 'jujudopix']

# Array de objetos
gamelist = [{'Título': 'CS-GO',
            'Ano': 2012,
             'Categoria': 'FPS Online'}]

consolelist = [{'Nome': 'PS5',
                'Preço': 5.000,
                'País': 'Brasil'}]


def init_app(app):
    # Criando a rota principal do site
    @app.route('/')
    # Criando função no Python
    # View function - Função de vizualização
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        # Acessando o primeiro jogo da lista de jogos
        game = gamelist[0]

        if request.method == 'POST':
            if request.form.get('jogador'):  # name da input
                jogadores.append(request.form.get('jogador'))

        jogos = ['Fortnite', 'League of Legends', 'CrossFire', 'Roblox',
                 'PUBG', 'Minecraft', 'Lost Ark', 'Counter-Strike: Global Offensive']

        return render_template('games.html', game=game, jogadores=jogadores, jogos=jogos)

    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():

        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título': request.form.get('titulo'), 'Ano': request.form.get(
                    'ano'), 'Categoria': request.form.get('categoria')})

        return render_template('cadgames.html', gamelist=gamelist)
    
    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():

        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('preco') and request.form.get('pais'):
                gamelist.append({'Nome': request.form.get('nome'), 'Preço': request.form.get(
                    'preco'), 'País': request.form.get('pais')})

        return render_template('consoles.html', consolelist=consolelist)
