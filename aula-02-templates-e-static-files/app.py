#comentario no Python
#importando o flask para a aplicação
from flask import Flask, render_template
#carregando o flask na variavel "app"
#Declarando variavel no python
app = Flask(__name__, template_folder= 'views')
#variaveis com __ são variaveis de ambiente do Python
#__name__ representa o nome da aplicação
#criando a rota principal do site
@app.route('/')
#def cria funções no python
def home():
    return render_template('index.html')

@app.route('/games')
def games():
    #criando variaveis para a rota de games
    titulo = "Portal 2"
    ano = 2011
    categoria = "Puzzle"
    
    jogadores = ['Marcos', 'Richard', 'Miguel', 'Renato', 'Pedro']
    #enviando as variaveis para o html
    return render_template('games.html', titulo = titulo, ano = ano, categoria = categoria, jogadores = jogadores)

@app.route('/consoles')
def consoles():
    #criando um onjeto
    console = {"Nome" : "Playstation 2", "Fabricante" : "Sony" , "Ano" : 2000}
    return render_template('consoles.html' , console= console)

#inciando o servidor na porta 5000

if __name__ == '__main__':
#está verificando se o arquivo gravado em "__name__ é o arquivo principal
    app.run(port=5000, debug=True)  
#o metodo .run() inicia o servidor