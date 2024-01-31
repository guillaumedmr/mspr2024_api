from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from config import Config
from models import db, Utilisateurs

app = Blueprint('auth_routes', __name__)

@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()

        prenom = data.get('prenom')
        nom = data.get('nom')
        dateNaissance = data.get('dateNaissance')
        email = data.get('email')
        mot_de_passe = data.get('mot_de_passe')

        new_user = Utilisateurs(
            prenom=prenom, 
            nom=nom,
            dateNaissance=dateNaissance,
            email=email,
            mot_de_passe=mot_de_passe
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify(message='Inscription réussie!')

    except Exception as e:
        return jsonify(error=f"Une erreur s'est produite : {str(e)}"), 500