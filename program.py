from flask import Flask, jsonify, request, send_file
from sqlalchemy.exc import SQLAlchemyError
import base64

from config import Config
from models import db, Image

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/upload_image/<image_name>', methods=['GET'])
def upload_image(image_name):
    image_path = f'images/{image_name}'
    
    try:
        with open(image_path, 'rb') as f:
            image_content = f.read()

        new_image = Image(img_blob=image_content)
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
    images = Image.query.all()
    image_list = [{'id': image.id, 'name': base64.b64encode(image.img_blob).decode('utf-8')} for image in images]
    return jsonify(images=image_list)

if __name__ == '__main__':
    app.run(debug=True)