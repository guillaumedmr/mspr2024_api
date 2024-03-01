DROP TABLE IF EXISTS `utilisateur`;
DROP TABLE IF EXISTS `animal`;
DROP TABLE IF EXISTS `empreinte`;

CREATE TABLE utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prenom VARCHAR(255) NOT NULL,
    nom VARCHAR(255) NOT NULL,
    dateNaissance DATE NOT NULL,
    email VARCHAR(255) NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL
);

CREATE TABLE animal (
    id_animal INT AUTO_INCREMENT NOT NULL,
    img_animal LONGBLOB NULL,
    statut_animal VARCHAR(255) NOT NULL,
    nom_animal VARCHAR(255) NOT NULL,
    nom_latin_animal VARCHAR(255) NOT NULL,
    habitat_animal VARCHAR(255) NOT NULL,
    region_animal VARCHAR(255) NOT NULL,
    funfact_animal VARCHAR(255) NOT NULL,
    description_animal VARCHAR(255) NOT NULL,
    taille_animal INT NOT NULL,
    CONSTRAINT animal_PK PRIMARY KEY (id_animal)
) ENGINE=InnoDB;

CREATE TABLE empreinte (
    id_empreinte INT AUTO_INCREMENT NOT NULL,
    coordonnee_empreinte VARCHAR(255) NULL,
    img_empreinte LONGBLOB NOT NULL,
    date_empreinte DATETIME NULL,
    id_animal INT NULL,
    id_utilisateur INT NULL,
    CONSTRAINT empreinte_PK PRIMARY KEY (id_empreinte),
    CONSTRAINT empreinte_animal_FK FOREIGN KEY (id_animal) REFERENCES animal(id_animal),
    CONSTRAINT empreinte_utilisateur0_FK FOREIGN KEY (id_utilisateur) REFERENCES utilisateurs(id)
) ENGINE=InnoDB;
