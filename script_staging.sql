CREATE TABLE stg_image (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_blob LONGBLOB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    coordinates VARCHAR(255) NULL,
    espece VARCHAR(255) NULL,
    user VARCHAR(255) NULL
);

CREATE TABLE stg_infos_espece (
	id INT AUTO_INCREMENT PRIMARY KEY,
    espece VARCHAR(255),
    description VARCHAR(255),
    nom_latin VARCHAR(255),
    famille VARCHAR(255),
    region VARCHAR(255),
    habitat VARCHAR(255),
    fun_fact VARCHAR(255),
    taille VARCHAR(255)
);