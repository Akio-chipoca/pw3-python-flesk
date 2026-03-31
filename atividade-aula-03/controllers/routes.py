    #importando o flask para a aplicação
from flask import render_template, request, redirect, url_for


    # criando a função principal para inicializar as rotas
def init_app(app):
        #criando a rota principal do site
        
    listainfos = ['Playstation 5', 'Xbox One', 'Super Nintendo', 'Atari', '3DS']
    
    listaMusicas = [{ 'titulo' : 'wet', 'ano' : 2017, 'categoria' : 'tristeza'}]
    @app.route('/')
        #def cria funções no python
    def home():
            return render_template('index.html')

    @app.route('/musicas')
    def Musicas():
            #criando variaveis para a rota de Musicas
            titulo = "Portal 2"
            ano = 2011
            categoria = "Romântica"
            
            ouvintes = ['Marcos', 'Richard', 'Miguel', 'Renato', 'Pedro']
            #enviando as variaveis para o html
            return render_template('musicas.html', titulo = titulo, ano = ano, categoria = categoria, ouvintes = ouvintes)

    @app.route('/infos', methods=['GET', 'POST'])
    def infos():
            #criando um onjeto
            infos = {"Nome" : "Playstation 2", "Fabricante" : "Sony" , "Ano" : 2000}
            
            #recebendo o valor do formulario
            if request.method == 'POST':
                if request.form.get('novainfo'):
                    listainfos.append(request.form.get)('novainfo')
            
            return render_template('infos.html' , infos=infos, listainfos=listainfos)
    @app.route('/cadmusicas', methods=['GET','POST'])
    def cadmusicas():
        # recebendo os dados do formulario e enviando para a pagina
        # verificando se a requisição sdo usuario pe do tipo POST
        if request.method == 'POST':
            #aqui ele irá gravar os dados na lista de jogos
            listaMusicas.append({'titulo' : request.form.get
            ('titulo'), 'ano' : request.form.get('ano'),
            'categoria' : request.form.get('categoria')})
            #aqui o usuario será redirecionado novamente para a página
            
            return redirect(url_for('cadmusicas'))
        return render_template('cadmusicas.html',
                               listaMusicas = listaMusicas)