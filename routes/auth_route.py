from flask import Blueprint, jsonify, request, make_response
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from flask import session
from datetime import datetime

from config import Config
from models.ModelDatawarehouse import Utilisateurs
from extensions import db, jwt
from routes.middleware import verify_token

auth_app = Blueprint('auth_routes', __name__)  

bcrypt = Bcrypt()

@auth_app.route('/signup', methods=['POST'])
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
    

@auth_app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        mot_de_passe = data.get('mot_de_passe')

        # Supposons que Utilisateurs utilise déjà 'datawarehouse' comme bind par défaut.
        user = Utilisateurs.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.mot_de_passe, mot_de_passe):
            access_token = create_access_token(identity=user.id)
            
            # Créer une réponse avec le message approprié et le token JWT dans le corps de la réponse
            response_body = jsonify(message='Connecté avec succès', access_token=access_token)
            response = make_response(response_body, 200)
            
            # Définir le cookie contenant le token
            response.set_cookie('access_token', access_token, httponly=True)  # httponly=True pour une meilleure sécurité
            
            return response
        else:
            return jsonify(message='Email ou mot de passe incorrect'), 401
    except Exception as e:
        return jsonify(error=f"Une erreur s'est produite : {str(e)}"), 500