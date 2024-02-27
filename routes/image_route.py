from flask import Blueprint, jsonify, request
from extensions import db  
from ModelDatawarehouse import Images  

image_app = Blueprint('image_routes', __name__)

@image_app.route('/upload_image', methods=['POST']) 
def upload_image():
    try:
        data = request.get_json()
        print(data)
        return jsonify(message='Image upload !')

    except Exception as e:
        return jsonify(error=f"Une erreur s'est produite : {str(e)}"), 500
