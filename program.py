from flask import Flask

from routes.image_route import app as image_app
from routes.auth_route import app as auth_app
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(auth_app, url_prefix='/auth')
app.register_blueprint(image_app, url_prefix='/images')

if __name__ == '__main__':
    app.run(debug=True)
