from flask import request, jsonify
from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity

def verify_token():
    def decorator(func):
        @wraps(func)
        @jwt_required()
        def wrapper(*args, **kwargs):
            try:
                # Récupérez l'identifiant de l'utilisateur à partir du token JWT.
                user_id = get_jwt_identity()
                
                # Passez l'identifiant de l'utilisateur à la route via kwargs.
                kwargs['user_id'] = user_id
                
                # Assurez-vous de retourner le résultat de l'appel de la fonction décorée.
                return func(*args, **kwargs)
            except Exception as e:
                return jsonify(message='Erreur lors de la vérification du token', error=str(e)), 401
        return wrapper
    return decorator
