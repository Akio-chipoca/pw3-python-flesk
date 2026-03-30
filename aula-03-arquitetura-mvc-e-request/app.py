#comentario no Python
#importando o flask para a aplicação
from flask import Flask, render_template
#carregando o flask na variavel "app"
#Declarando variavel no python
app = Flask(__name__, template_folder= 'views')
#variaveis com __ são variaveis de ambiente do Python
#__name__ representa o nome da aplicação
from controllers import routes
# enviando a variavel app para as rotas
routes.init_app(app)

#inciando o servidor na porta 5000

if __name__ == '__main__':
#está verificando se o arquivo gravado em "__name__ é o arquivo principal
    app.run(port=5000, debug=True)  
#o metodo .run() inicia o servidor