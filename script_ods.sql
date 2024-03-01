CREATE TABLE ods_image (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_blob LONGBLOB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    coordinates VARCHAR(255) NULL,
    espece VARCHAR(255) NULL,
    user VARCHAR(255) NULL
);

CREATE TABLE ods_infos_espece (
	id INT AUTO_INCREMENT PRIMARY KEY,
    espece VARCHAR(255),
    description TEXT,
    nom_latin VARCHAR(255),
    famille VARCHAR(255),
    region VARCHAR(255),
    habitat TEXT,
    fun_fact TEXT,
    taille_cm FLOAT
);