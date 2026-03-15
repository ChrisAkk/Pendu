# ici on va faire toutes les routes et c'est ici que vous devriez coder. 
# Tous ce qui est déjà présent et que vous ne comprenais pas c'est que c'est pour flask
# Ne toucher à rien je vous expliquerai tout.

from flask import Blueprint, render_template, request

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def welcome():
    return render_template('index.html')

@routes_bp.route('/game', methods=['POST'])
def to_game():
    theme = request.form.get('theme').split(',')
    essais = request.form.get('essais')
    caractere = request.form.get('caractere')
    indice = request.form.get('indice')
    aleatoire = request.form.get('aleatoire')
    print(theme, essais, caractere, indice, aleatoire)
    return render_template('game.html', theme=theme, essais=essais, caractere=caractere, indice=indice, aleatoire=aleatoire)