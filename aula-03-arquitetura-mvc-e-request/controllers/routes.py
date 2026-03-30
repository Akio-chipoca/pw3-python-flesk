    #importando o flask para a aplicação
from flask import render_template, request, redirect, url_for


    # criando a função principal para inicializar as rotas
def init_app(app):
        #criando a rota principal do site
        
    listaConsoles = ['Playstation 5', 'Xbox One', 'Super Nintendo', 'Atari', '3DS']
    
    listaGames = [{ 'titulo' : 'CS-GO', 'ano' : 2012, 'categoria' : 'FPS-Online', 'plataforma' : 'PC(Windows)'}]
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

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
            #criando um onjeto
            consoles = {"Nome" : "Playstation 2", "Fabricante" : "Sony" , "Ano" : 2000}
            
            #recebendo o valor do formulario
            if request.method == 'POST':
                if request.form.get('novoConsole'):
                    listaConsoles.append(request.form.get)('novoConsole')
            
            return render_template('consoles.html' , consoles=consoles, listaConsoles=listaConsoles)
    @app.route('/cadgames', methods=['GET','POST'])
    def cadgames():
        # recebendo os dados do formulario e enviando para a pagina
        # verificando se a requisição sdo usuario pe do tipo POST
        if request.method == 'POST':
            #aqui ele irá gravar os dados na lista de jogos
            listaGames.append({'titulo' : request.form.get
            ('titulo'), 'ano' : request.form.get('ano'),
            'categoria' : request.form.get('categoria'),
            'plataforma' : request.form.get('plataforma')})
            #aqui o usuario será redirecionado novamente para a página
            
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               listaGames = listaGames)