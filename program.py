# program.py
from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, jwt
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.secret_key = os.getenv("SESSION_SECRET_KEY")

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.config.from_object(Config)

    app.config['SQLALCHEMY_BINDS'] = {
        'staging': Config.SQLALCHEMY_DATABASE_URI_STAGING,
        'datawarehouse': Config.SQLALCHEMY_DATABASE_URI_DATAWAREHOUSE,
    }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY

    db.init_app(app)
    jwt.init_app(app)

    # Importation et enregistrement des blueprints ici, après l'initialisation de db et jwt
    from routes.auth_route import auth_app
    from routes.user_route import user_app
    from routes.image_route import image_app

    app.register_blueprint(auth_app, url_prefix='/auth')
    app.register_blueprint(user_app, url_prefix='/user')
    app.register_blueprint(image_app, url_prefix='/images')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
