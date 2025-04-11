# Importando o Flask
from flask import Flask, render_template
# Importanto o PyMySQL
import pymysql
# Importando as rotas que estão nos controllers
from controllers import routes
# Importando o models
from models.database import db
# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

# Chamando as rotas
routes.init_app(app)

# Define o nome do banco de dados
DB_NAME = 'games'
#Configura o Flask com o Banco definido
app.config['DATABASE_NAME'] = DB_NAME

# Passando o endereço do banco ao Flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:root@localhost/{DB_NAME}'

# Iniciando o servidor no localhost, porta 5000, modo de depuração ativado
if __name__ == '__main__':
    # Criando os dados de conexão com o banco de dados
    connection = pymysql.connect(host='localhost', user='root', password='', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    # Tentando criar o banco de dados
    #Try, trata com sucesso
    try:
        # with cria um recurso temporariamente
        with connection.cursor() as cursor:
            # Criando o banco de dados (se ele não existir)
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
            print(f"Banco de dados {DB_NAME} criado com sucesso!")
            # Criando a tabela de jogos (se ela não existir)
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS games (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    titluo VARCHAR(150),
                    ano INT,
                    categoria VARCHAR(150),
                    paltaforma VARCHAR(150),
                    preco FLOAT,
                    descricao TEXT
                );
            """)
    #Except, trata com falha
    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        connection.close()
        
    # Pasando o flask para SQLAlchemy
    db.init_app(app)
    
    # Criando as tabelas a partir do model
    with app.test_request_context():
        db.create_all()
        print("Tabelas criadas com sucesso!")
    
    # Inicializando a aplicação Flask
    app.run(host='localhost', port=5000, debug=True)
