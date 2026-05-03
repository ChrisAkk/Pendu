from flask import Blueprint, render_template, request, session
from dictionnaire import dictionnaire_des_mots
from random import choice, randint

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def welcome():
    if 'historique' not in session:
        session['historique'] = []

    return render_template('index.html', historique=session['historique'])

@routes_bp.route('/game', methods=['POST'])
def to_game():
    ''' Cette fonction doit uniquement renvoyer la page de jeu en trouvant le mot grace aux infos rentrer dans le panneau de configuration'''

    session['compteur'] = 0
    session['lettre_selectionne'] = []
    session['image_index'] = 0
    session['ticket_triche'] = randint(0, 10_000)

    # theme
    session['theme'] = choice(request.form.get('theme').split(','))

    # caractere
    session['caractere'] = request.form.get('caractere')
    session['aleatoire'] = request.form.get('aleatoire')
    if session['aleatoire'] == 'on':
        session['caractere'] = str(randint(1, 3))
    
    if session['caractere'] == '1':
        session['caractere'] = '4_6'
    elif session['caractere'] == '2':
        session['caractere'] = '7_10'
    else:
        session['caractere'] = '11_et_plus' 

    # mot
    session['mot'] = choice(list(dictionnaire_des_mots[session['theme']][session['caractere']].keys()))
    session['mot_cache'] = ['_' if l not in [' ', "'"] else l for l in session['mot']]

    # indice 
    session['indice'] = request.form.get('indice')
    if session['indice'] == 'on':
        session['indice'] = dictionnaire_des_mots[session['theme']][session['caractere']][session['mot']]
    else:
        session['indice'] = None

    # essais
    session['essais'] = request.form.get('essais')
    session['nombre_essais_restant'] = int(session['essais'])
    win = None
    
    return render_template('game.html', 
                           mot=session['mot'], 
                           indice=session['indice'], 
                           essais=session['essais'], 
                           mot_cache=session['mot_cache'], 
                           win=win, 
                           lettre_selectionne=session['lettre_selectionne'], 
                           image_index=session['image_index'], 
                           ticket_triche=session['ticket_triche'])

@routes_bp.route('/take_chance', methods=['POST'])
def take_chance():
    ''' Cette fonction doit voir si la lettre est dans le mot ou pas'''

    win = None
    lettre_dans_mot = False
    lettre = request.form.get('letters')

    lettre_selectionne = session['lettre_selectionne']
    lettre_selectionne.append(lettre)
    session['lettre_selectionne'] = lettre_selectionne

    ticket = request.form.get('ticket')
    compteur = session['compteur']
    essais = session['essais']

    historique = session['historique']

    if int(ticket) != session['ticket_triche'] :
        return render_template('triche.html')
    else:
        session['ticket_triche'] += 1

    if int(essais) > compteur:
        mot = session['mot']
        for i in range(len(mot)):
            if lettre == mot[i]:
                mot_cache = session['mot_cache']
                mot_cache[i] = lettre
                session['mot_cache'] = mot_cache
                lettre_dans_mot = True

        if not lettre_dans_mot:
            compteur += 1
            session['nombre_essais_restant'] = int(essais) - int(compteur)
            session['image_index'] = int(round(compteur * (12 / int(essais))))
            
            if compteur >= int(essais):
                win = False
                historique.append(f"Défaite en {essais} fautes sur {essais} sur le mot : {mot}.")

            session['compteur'] = compteur

        if ''.join(session['mot_cache']) == mot:
            win = True
            historique.append(f"Victoire en {session['compteur']} fautes sur {session['essais']} sur le mot : {mot}.")   

        session['historique'] = historique   
        session.modified = True

        if lettre_dans_mot == True:
            lettre_dans_mot = '1'
        else:
            lettre_dans_mot = '0'    
        
        return render_template('game.html', 
                                lettre=lettre, 
                                essais=essais, 
                                mot=mot, 
                                mot_cache=session['mot_cache'], 
                                win=win, 
                                nombre_essais_restant=session['nombre_essais_restant'], 
                                lettre_selectionne=session['lettre_selectionne'], 
                                image_index=session['image_index'], 
                                ticket_triche=session['ticket_triche'],
                                indice=session['indice'],
                                theme=session['theme'],
                                caractere=session['caractere'],
                                aleatoire=session['aleatoire'],
                                compteur=compteur,
                                lettre_dans_mot=lettre_dans_mot
                               )