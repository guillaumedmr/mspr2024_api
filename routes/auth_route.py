from flask import Blueprint, jsonify, request
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

from config import Config
from models import db, Utilisateurs

app = Blueprint('auth_routes', __name__)

bcrypt = Bcrypt()

@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()

        prenom = data.get('prenom')
        nom = data.get('nom')
        dateNaissance = data.get('dateNaissance')
        email = data.get('email')
        mot_de_passe = data.get('mot_de_passe')

        existing_user = Utilisateurs.query.filter_by(email=email).first()
        if existing_user:
            return jsonify(message='Cet utilisateur existe déjà! Veuillez choisir un autre email.'), 400

        hashed_password = bcrypt.generate_password_hash(mot_de_passe).decode('utf-8')

        new_user = Utilisateurs(
            prenom=prenom, 
            nom=nom,
            dateNaissance=dateNaissance,
            email=email,
            mot_de_passe=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify(message='Inscription réussie!')

    except IntegrityError as e:
        db.session.rollback()
        return jsonify(message='Erreur d\'intégrité: Cet utilisateur existe déjà!'), 400

    except Exception as e:
        return jsonify(error=f"Une erreur s'est produite : {str(e)}"), 500