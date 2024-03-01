from flask_sqlalchemy import SQLAlchemy
from extensions import db

class Utilisateurs(db.Model):
    __bind_key__ = 'datawarehouse' 
    id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(255), nullable=False)
    nom = db.Column(db.String(255), nullable=False)
    dateNaissance = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)

class Animal(db.Model):
    __bind_key__ = 'datawarehouse'
    id_animal = db.Column(db.Integer, primary_key=True)
    img_animal = db.Column(db.LargeBinary, nullable=True)
    statut_animal = db.Column(db.String(255), nullable=False)
    nom_animal = db.Column(db.String(255), nullable=False)
    nom_latin_animal = db.Column(db.String(255), nullable=False)
    habitat_animal = db.Column(db.String(255), nullable=False)
    region_animal = db.Column(db.String(255), nullable=False)
    funfact_animal = db.Column(db.String(255), nullable=False)
    description_animal = db.Column(db.String(255), nullable=False)
    taille_animal = db.Column(db.Integer, nullable=False)

class Empreinte(db.Model):
    __bind_key__ = 'datawarehouse'
    id_empreinte = db.Column(db.Integer, primary_key=True)
    coordonnee_empreinte = db.Column(db.String(255), nullable=True)
    img_empreinte = db.Column(db.LargeBinary, nullable=False)
    date_empreinte = db.Column(db.DateTime, nullable=True)
    id_animal = db.Column(db.Integer, db.ForeignKey('animal.id_animal'), nullable=True)
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateurs.id'), nullable=True)
