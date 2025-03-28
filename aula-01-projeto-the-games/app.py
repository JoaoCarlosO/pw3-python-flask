# Comentário em Python
# Importando o pacote do Flask
from flask import Flask, render_template

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

# Criando a rota principal do site


@app.route('/')
# Criando função no Python
# View function - Função de vizualização
def home():
    return render_template('index.html')


@app.route('/games')
def games():
    # Dicionário no Python(obejto)
    game = {'Título': 'CS-GO',
            'Ano': 2012,
            'Categoria': 'FPS Online'}
    jogadores = ['iruh', 'davi_lambari', 'edsongf',
                 'kioto', 'black butterfly', 'jujudopix']
    jogos = ['Fortnite', 'League of Legends', 'CrossFire', 'Roblox',
             'PUBG', 'Minecraft', 'Lost Ark', 'Counter-Strike: Global Offensive']

    return render_template('games.html', game=game, jogadores=jogadores, jogos=jogos)


if __name__ == '__main__':
    # Rodando o servidor na localhost, porta 5000
    app.run(host='localhost', port=5000, debug=True)
