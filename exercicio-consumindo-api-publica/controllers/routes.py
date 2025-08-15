from flask import render_template, request, url_for, redirect
from models.database import musica, db
import urllib
import json


def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/musicas', methods=['GET', 'POST'])
    def musicas():
        musica = musicalist[0]

        return redirect(url_for('musicas'))
        return render_template('musicas.html',
                           musica=musica,)

    # Rota de API de jogos


    @app.route('/apimusicas', methods=['GET', 'POST'])
    @app.route('/apimusicas/<int:id>', methods=['GET', 'POST'])
    def apimusicas(id=None):
        url = 'https://www.freetogame.com/api/games'
        response = urllib.request.urlopen(url)
        apiData = response.read()
        musicalist = json.loads(apiData)
        # Se id existir (ou seja, foi informado parâmetro)
        if id:
            musicaInfo = []
            for musica in musicalist:
                if musica['id'] == id:
                    musicaInfo = musica
                    break
            if musicaInfo:
                return render_template('musicasInfo.html', musicaInfo=musicaInfo)
            else:
             return f'Game com a ID {id} não foi encontrado.'
        else:
            return render_template('apigames.html', gameList=musicalist)
