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



