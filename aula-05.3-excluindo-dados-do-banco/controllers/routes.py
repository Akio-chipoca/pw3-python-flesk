# importando o flask para a aplicação
from flask import render_template, request, redirect, url_for

from models.database import Game, Console, db


# criando a função principal para inicializar as rotas
def init_app(app):

    listaConsoles = ['Playstation 5', 'Xbox One', 'Super Nintendo', 'Atari', '3DS']

    listaGames = [{
        'titulo': 'CS-GO',
        'ano': 2012,
        'categoria': 'FPS-Online',
        'plataforma': 'PC(Windows)'
    }]

    # rota principal
    @app.route('/')
    def home():
        return render_template('index.html')

    # rota games
    @app.route('/games')
    def games():

        titulo = "Portal 2"
        ano = 2011
        categoria = "Puzzle"

        jogadores = ['Marcos', 'Richard', 'Miguel', 'Renato', 'Pedro']

        return render_template(
            'games.html',
            titulo=titulo,
            ano=ano,
            categoria=categoria,
            jogadores=jogadores
        )

    # rota consoles
    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():

        consoles = {
            "Nome": "Playstation 2",
            "Fabricante": "Sony",
            "Ano": 2000
        }

        if request.method == 'POST':

            if request.form.get('novoConsole'):
                listaConsoles.append(
                    request.form.get('novoConsole')
                )

        return render_template(
            'consoles.html',
            consoles=consoles,
            listaConsoles=listaConsoles
        )

    # cadastro de games
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():

        if request.method == 'POST':

            listaGames.append({
                'titulo': request.form.get('titulo'),
                'ano': request.form.get('ano'),
                'categoria': request.form.get('categoria'),
                'plataforma': request.form.get('plataforma')
            })

            return redirect(url_for('cadgames'))

        return render_template(
            'cadgames.html',
            listaGames=listaGames
        )

    # estoque
    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/delete/<int:id>')
    def estoque(id=None):

        # deletar console
        if id:

            console = Console.query.get(id)

            db.session.delete(console)
            db.session.commit()

            return redirect(url_for('estoque'))

        # cadastrar console
        if request.method == 'POST':

            dados = request.form.to_dict()

            newconsole = Console(
                dados['nome'],
                dados['fabricante'],
                dados['ano'],
                dados['preco'],
                dados['quantidade']
            )

            db.session.add(newconsole)
            db.session.commit()

            return redirect(url_for('estoque'))

        # listar consoles
        consoles = Console.query.all()

        return render_template(
            'estoque.html',
            consoles=consoles
        )

    # editar
    @app.route('/estoque/editar', methods=['GET', 'POST'])
    def editar():

        return render_template('editGame.html')