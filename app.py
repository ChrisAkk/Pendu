# je vais tout faire ici vous inquietez pas (c'est pour lancer l'app web)

from flask import Flask
from routes import routes_bp

app = Flask(__name__)
app.register_blueprint(routes_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5002)