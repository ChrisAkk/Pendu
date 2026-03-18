# ici on va faire toutes les routes et c'est ici que vous devriez coder. 
# Tous ce qui est déjà présent et que vous ne comprenais pas c'est que c'est pour flask
# Ne toucher à rien je vous expliquerai tout.

from flask import Blueprint, render_template, request
from dictionnaire import dictionnaire_des_mots

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def welcome():
    return render_template('index.html')

@routes_bp.route('/game', methods=['POST'])
def to_game():
    ''' Cette fonction doit uniquement renvoyer la page de jeu en trouvant le mot grace aux infos rentrer dans le panneau de configuration'''
    theme = request.form.get('theme').split(',')
    essais = request.form.get('essais')
    caractere = request.form.get('caractere')
    indice = request.form.get('indice')
    aleatoire = request.form.get('aleatoire')
    
    return render_template('game.html')

@routes_bp.route('/take_chance', methods=['POST'])
def take_chance():
    ''' Cette fonction doit voir si la lettre est dans le mot ou pas'''
    lettre = request.form.get('letters')
    return render_template('game.html', lettre=lettre)
