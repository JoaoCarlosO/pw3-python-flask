from flask import render_template, request, url_for, redirect
from models.database import Musica, db
import urllib.request
import json
import urllib.parse


def init_app(app):
    @app.route('/')
    def home():
        return render_template('base.html')

    @app.route('/apimusicas', methods=['GET', 'POST'])
    @app.route('/apimusicas/<int:id>', methods=['GET'])
    def apimusicas(id=None):
        # Detalhe da música
        if id is not None:
            url = f"https://api.deezer.com/track/{id}"
            with urllib.request.urlopen(url) as resp:
                dados = json.loads(resp.read().decode("utf-8"))

            # Se houver erro na API
            if isinstance(dados, dict) and dados.get("error"):
                return f"Não encontrei a música com ID {id}.", 404

            return render_template("musicaInfo.html", musicaInfo=dados)

        # Lista de músicas (busca)
        search = request.form.get("search") or request.args.get("search") or "bruno mars"
        url = f"https://api.deezer.com/search?q={urllib.parse.quote(search)}"
        with urllib.request.urlopen(url) as resp:
            dados = json.loads(resp.read().decode("utf-8"))

        musicalist = dados.get("data", [])
        return render_template("apimusicas.html", musicalist=musicalist, search=search)