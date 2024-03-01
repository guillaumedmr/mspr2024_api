from flask import Blueprint, jsonify, request, make_response
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from flask import session
import base64
from datetime import datetime

from config import Config
from models.ModelDatawarehouse import Utilisateurs, Empreinte, Animal
from extensions import db, jwt
from routes.middleware import verify_token
from utils.ville_plus_proche import ville_plus_proche

user_app = Blueprint('user_route', __name__)  

@user_app.route('/get_info', methods=['GET']) 
@verify_token()  
def get_info(**kwargs):
    try:
        user_id = kwargs['user_id']

        user = Utilisateurs.query.filter_by(id=user_id).first()

        formatted_date = user.dateNaissance.strftime("%d-%m-%Y")

        user_data = {
            'id': user.id,
            'nom': user.nom,
            'prenom': user.prenom,
            'dateNaissance': formatted_date,
            'email': user.email,            
        }

        return jsonify(message='Informations récupérées !', user=user_data), 200

    except Exception as e:
        return jsonify(error=f"Une erreur s'est produite : {str(e)}"), 500


@user_app.route('/get_historique', methods=['GET']) 
@verify_token()  
def get_historique(**kwargs):
    try:
        user_id = kwargs['user_id']

        # Requête pour récupérer l'utilisateur
        utilisateur = Utilisateurs.query.get(user_id)

        if utilisateur is None:
            return jsonify(error="Utilisateur non trouvé"), 404

        # Requête pour récupérer toutes les empreintes de l'utilisateur
        user_historique = Empreinte.query.filter_by(id_utilisateur=user_id).all()

        # Trier les empreintes par date de manière décroissante
        user_historique.sort(key=lambda x: x.date_empreinte, reverse=True)

        # Construction de la correspondance entre les IDs des animaux et leurs noms
        animaux = {animal.id_animal: {'nom': animal.nom_animal, 'fun_fact': animal.funfact_animal} for animal in Animal.query.all()}

        historique = []
        for empreinte in user_historique:
            coordonnees = [float(coord) for coord in empreinte.coordonnee_empreinte.strip('[]').split(',')] if empreinte.coordonnee_empreinte else None
            nom_ville = ville_plus_proche(coordonnees) if coordonnees else 'Pas de localisation'
            # Conversion de l'image en base64
            img_base64 = base64.b64encode(empreinte.img_empreinte).decode('utf-8') if empreinte.img_empreinte else None
            historique.append({
                'base64': img_base64,
                'date_empreinte': empreinte.date_empreinte.strftime("%d-%m-%Y %H:%M:%S"),
                'nom_animal': animaux.get(empreinte.id_animal, {}).get('nom'),
                'coordonnee_empreinte': nom_ville,
                'fun_fact': animaux.get(empreinte.id_animal, {}).get('fun_fact'),
            })

        return jsonify(message='Informations récupérées !', user_historique=historique), 200

    except Exception as e:
        return jsonify(error=f"Une erreur s'est produite : {str(e)}"), 500


@user_app.route('/get_feed', methods=['GET']) 
def get_feed():
    try:
        # Récupération de toutes les empreintes de tous les utilisateurs
        all_historiques = []
        for utilisateur in Utilisateurs.query.all():
            user_historique = Empreinte.query.filter_by(id_utilisateur=utilisateur.id).all()

            animaux = {animal.id_animal: {'nom': animal.nom_animal, 'fun_fact': animal.funfact_animal} for animal in Animal.query.all()}

            historique = []
            for empreinte in user_historique:
                coordonnees = [float(coord) for coord in empreinte.coordonnee_empreinte.strip('[]').split(',')] if empreinte.coordonnee_empreinte else None
                nom_ville = ville_plus_proche(coordonnees) if coordonnees else 'Pas de localisation'
                # Conversion de l'image en base64
                img_base64 = base64.b64encode(empreinte.img_empreinte).decode('utf-8') if empreinte.img_empreinte else None
                historique.append({
                    # 'base64': img_base64,
                    'date_empreinte': empreinte.date_empreinte.strftime("%d-%m-%Y %H:%M:%S"),
                    'nom_animal': animaux.get(empreinte.id_animal, {}).get('nom'),
                    'coordonnee_empreinte': nom_ville,
                    'fun_fact': animaux.get(empreinte.id_animal, {}).get('fun_fact'),
                    'user': utilisateur.nom + ' ' + utilisateur.prenom,
                })

            all_historiques.extend(historique)

        # Tri par date décroissante
        all_historiques.sort(key=lambda x: datetime.strptime(x['date_empreinte'], "%d-%m-%Y %H:%M:%S"), reverse=True)

        return jsonify(message='Informations récupérées !', feed=all_historiques), 200

    except Exception as e:
        return jsonify(error=f"Une erreur s'est produite : {str(e)}"), 500


