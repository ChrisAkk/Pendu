# ici on va faire toutes les routes et c'est ici que vous devriez coder. 
# Tous ce qui est déjà présent et que vous ne comprenais pas c'est que c'est pour flask
# Ne toucher à rien je vous expliquerai tout.

from flask import Blueprint, render_template

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def welcome():
    return render_template('index.html')

