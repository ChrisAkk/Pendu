# je vais tout faire ici vous inquietez pas (c'est pour lancer l'app web)

from flask import Flask, session
from routes import routes_bp
import os

app = Flask(__name__)
app.register_blueprint(routes_bp)
app.secret_key = os.getenv('SECRET_KEY', 'tu_ne_trouvera_jamais_cette_cle')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(debug=True, port=port)
