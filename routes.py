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
nombre_essais_restant = 0
lettre_selectionne = []
image_index = 0
ticket_triche = 0

@routes_bp.route('/')
def welcome():
    return render_template('index.html')

@routes_bp.route('/game', methods=['POST'])
def to_game():
    ''' Cette fonction doit uniquement renvoyer la page de jeu en trouvant le mot grace aux infos rentrer dans le panneau de configuration'''
    global mot, essais, mot_cache, lettre_selectionne, image_index, compteur, ticket_triche

    compteur = 0
    lettre_selectionne = []
    image_index = 0
    ticket_triche = randint(0, 10_000)

    # theme
    theme = choice(request.form.get('theme').split(','))

    # caractere
    caractere = request.form.get('caractere')
    aleatoire = request.form.get('aleatoire')
    if aleatoire == 'on':
        caractere = randint(1, 3)
    
    if int(caractere) == 1:
        caractere = '4_6'
    elif int(caractere) == 2:
        caractere = '7_10'
    else:
        caractere = '11_et_plus'

    # mot
    mot = choice(list(dictionnaire_des_mots[theme][caractere].keys()))
    mot_cache = ['_' if l != ' ' else ' ' for l in mot]

    # indice 
    indice = request.form.get('indice')
    if indice == 'on':
        indice = dictionnaire_des_mots[theme][caractere][mot]
    else:
        indice = None

    # essais
    essais = request.form.get('essais')
    win = None
    
    return render_template('game.html', mot=mot, indice=indice, essais=essais, mot_cache=mot_cache, win=win, lettre_selectionne=lettre_selectionne, image_index=image_index, ticket_triche=ticket_triche)

@routes_bp.route('/take_chance', methods=['POST'])
def take_chance():
    ''' Cette fonction doit voir si la lettre est dans le mot ou pas'''
    global mot, essais, mot_cache, compteur, win, nombre_essais_restant, lettre_selectionne, image_index, ticket_triche
    win = None
    lettre_dans_mot = False
    lettre = request.form.get('letters')
    lettre_selectionne.append(lettre)
    ticket = request.form.get('ticket')

    if int(ticket) != ticket_triche :
        return render_template('index.html')
    else:
        ticket_triche += 1

    if int(essais) > compteur + 1:

        for i in range(len(mot)):
            if lettre == mot[i]:
                mot_cache[i] = lettre
                lettre_dans_mot = True

        if not lettre_dans_mot:
            compteur += 1
            nombre_essais_restant = int(essais) - int(compteur)
            image_index = int(round(compteur * (12 / int(essais))))
            print(image_index)

        if ''.join(mot_cache) == mot:
            win = True
            return render_template('game.html', 
                                   lettre=lettre, 
                                   essais=essais, 
                                   mot=mot, 
                                   mot_cache=mot_cache, 
                                   win=win, 
                                   nombre_essais_restant=nombre_essais_restant, 
                                   image_index=image_index, 
                                   ticket_triche=ticket_triche
                                   )
        
        return render_template('game.html', 
                               lettre=lettre, 
                               essais=essais, 
                               mot=mot, 
                               mot_cache=mot_cache, 
                               win=win, 
                               nombre_essais_restant=nombre_essais_restant, 
                               lettre_selectionne=lettre_selectionne, 
                               image_index=image_index, 
                               ticket_triche=ticket_triche
                               )
    
    else : 
        win = False
        return render_template('game.html', 
                               lettre=lettre, 
                               essais=essais, 
                               mot=mot, 
                               mot_cache=mot_cache, 
                               win=win, 
                               nombre_essais_restant=nombre_essais_restant, 
                               image_index=image_index, 
                               ticket_triche=ticket_triche
                               ) 
 