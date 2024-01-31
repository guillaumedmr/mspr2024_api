from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
import base64
import numpy as np
import io
import tensorflow as tf

from PIL import Image
from io import BytesIO

from config import Config
from models import db, Images

app = Blueprint('image_routes', __name__)

@app.route('/upload_image/<image_name>', methods=['GET'])
def upload_image(image_name):
    image_path = f'images/{image_name}'
    
    try:
        with open(image_path, 'rb') as f:
            image_content = f.read()

        new_image = Images(img_blob=image_content)
        db.session.add(new_image)
        db.session.commit()
        return jsonify(message="L'image a bien été uploadée !")
    except FileNotFoundError:
        return jsonify(error='Image not found'), 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(error=f"Erreur de base de données : {str(e)}"), 500
    except Exception as e:
        return jsonify(error=f"Une erreur inattendue s'est produite : {str(e)}"), 500

@app.route('/get_all_images', methods=['GET'])
def get_all_images():
    images = Images.query.all()
    image_list = [{'id': image.id, 'img_blob': image.img_blob} for image in images]

    # Prétraitement des images
    images = []
    for blob in image_list:
        image = Image.open(io.BytesIO(blob['img_blob']))
        image = np.array(image)
        images.append(image)
    
    images = np.array(images) / 255.0

    dataset = tf.data.Dataset.from_tensor_slices(images)
    
    return dataset
