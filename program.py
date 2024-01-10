from flask import Flask, jsonify, request, send_file
from sqlalchemy.exc import SQLAlchemyError
import base64

from config import Config
from models import db, Image

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)