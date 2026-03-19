# ici on va faire toutes les routes et c'est ici que vous devriez coder. 
# Tous ce qui est déjà présent et que vous ne comprenais pas c'est que c'est pour flask
# Ne toucher à rien je vous expliquerai tout.

from flask import Blueprint, render_template, request
from dictionnaire import dictionnaire_des_mots
from random import choice, randint

routes_bp = Blueprint('routes', __name__)
mot = ''
essais = 0
compteur = 0

@routes_bp.route('/')
def welcome():
    return render_template('index.html')

@routes_bp.route('/game', methods=['POST'])
def to_game():
    ''' Cette fonction doit uniquement renvoyer la page de jeu en trouvant le mot grace aux infos rentrer dans le panneau de configuration'''
    global mot, essais, mot_cache

    # theme
    theme = choice(request.form.get('theme').split(','))

    # caractere
    caractere = request.form.get('caractere')
    aleatoire = request.form.get('aleatoire')
    if aleatoire == 'on':
        caractere = randint(1, 3)
    
    if caractere == 1:
        caractere = '4_6'
    elif caractere == 2:
        caractere = '7_10'
    else:
        caractere = '11_et_plus'

    # mot
    mot = choice(list(dictionnaire_des_mots[theme][caractere].keys()))
    mot_cache = ['_' for l in mot]

    # indice 
    indice = request.form.get('indice')
    if indice == 'on':
        indice = dictionnaire_des_mots[theme][caractere][mot]
    else:
        indice = None

    # essais
    essais = request.form.get('essais')
    
    return render_template('game.html', mot=mot, indice=indice, essais=essais, mot_cache=mot_cache)

@routes_bp.route('/take_chance', methods=['POST'])
def take_chance():
    ''' Cette fonction doit voir si la lettre est dans le mot ou pas'''
    global mot, essais, mot_cache, compteur

    win = None
    lettre = request.form.get('letters')

    if int(essais) > compteur:

        for i in range(len(mot)):
            if lettre == mot[i]:
                mot_cache[i] = lettre

        if ''.join(mot_cache) == mot:
            print("c'est pareil")
            mot, mot_cache = '', []
            win = True
            compteur = 0
            return render_template('game.html', lettre=lettre, essais=essais, mot=mot, mot_cache=mot_cache, win=win)
        
        compteur += 1
        return render_template('game.html', lettre=lettre, essais=essais, mot=mot, mot_cache=mot_cache, win=win)
    
    else : 
        mot, mot_cache = '', []
        win = False
        compteur = 0
        return render_template('game.html', lettre=lettre, essais=essais, mot=mot, mot_cache=mot_cache, win=win) 
