# Comentário em Python
# Importando o pacote do Flask
from flask import Flask

# Carregando o Flask na variável app
app = Flask(__name__)

# Criando a rota principal do site
@app.route('/')
# Criando função no Python
def home():
    return '<h1>Meu primeiro site em Flask. Seja bem-vindo!</h1>'

@app.route('/games')

def games():
    return '<h1> Seja bem-vindo a página de games</h1>'

if __name__ == '__main__':
    # Rodando o servidor na localhost, porta 5000
    app.run(host = 'localhost', port = 5000, debug = True)
    