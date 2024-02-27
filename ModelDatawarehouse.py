from flask_sqlalchemy import SQLAlchemy
from extensions import db

class Images(db.Model):
    __bind_key__ = 'datawarehouse'  
    id = db.Column(db.Integer, primary_key=True)
    img_blob = db.Column(db.LargeBinary, nullable=False)
    espece = db.Column(db.String(255))

class Utilisateurs(db.Model):
    __bind_key__ = 'datawarehouse' 
    id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(255), nullable=False)
    nom = db.Column(db.String(255), nullable=False)
    dateNaissance = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
