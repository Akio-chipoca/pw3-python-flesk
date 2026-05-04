#comentario no Python
#importando o flask para a aplicação
from flask import Flask, render_template

import pymysql
#carregando o flask na variavel "app"
from models.database import db, Game
#Declarando variavel no python
DB_NAME = 'thegames'

from controllers import routes

app = Flask(__name__, template_folder= 'views')
#variaveis com __ são variaveis de ambiente do Python
#__name__ representa o nome da aplicação

app.config['DATABASE_NAME'] = DB_NAME


app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

# enviando a variavel app para as rotas
routes.init_app(app)

#inciando o servidor na porta 5000

if __name__ == '__main__':
    
    connection = pymysql.connect(host = 'localhost',
                                 user = 'root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    
    
    try:
        with connection.cursor() as cursor :
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME}')
            print("O banco de dados foi criado!")
    except Exception as error:
        print(f"Ocorreu um erro ao criar o banco de dados! {error}")
        
    finally:
        connection.close()
        
    db.init_app(app=app)
    
    with app.test_request_context():
        db.create_all()
    
#está verificando se o arquivo gravado em "__name__ é o arquivo principal
    app.run(port=5000, debug=True)  
#o metodo .run() inicia o servidor