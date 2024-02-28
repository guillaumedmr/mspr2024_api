from flask import Blueprint, jsonify, request
from extensions import db  
from models.ModelStaging import StgImage  
from .middleware import verify_token

image_app = Blueprint('image_routes', __name__)

@image_app.route('/upload_image', methods=['POST']) 
@verify_token()  
def upload_image(**kwargs):
    try:
        # Obtenir l'user_id à partir des attributs de la requête
        user_id = kwargs['user_id']

        data = request.get_json()

        # Encodage de l'image en base64
        image_blob_base64 = data['base64'].encode()

        coordinates = "[{},{}]".format(data['latitude'], data['longitude'])

        newImage = StgImage(
            image_blob=image_blob_base64,
            coordinates=coordinates,
            user="USER-"+str(user_id),
        )

        db.session.add(newImage)
        db.session.commit()

        return jsonify(message='Image upload !'), 200

    except Exception as e:
        return jsonify(error=f"Une erreur s'est produite : {str(e)}"), 500
