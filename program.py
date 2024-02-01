from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager   

from routes.image_route import app as image_app
from routes.auth_route import app as auth_app
from config import Config
from models import db

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://4010-37-174-251-7.ngrok-free.app"}})
app.config.from_object(Config)

app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

db.init_app(app)

jwt = JWTManager(app)

app.register_blueprint(auth_app, url_prefix='/auth')
app.register_blueprint(image_app, url_prefix='/images')

if __name__ == '__main__':
    app.run(debug=True)
