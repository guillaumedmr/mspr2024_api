CREATE TABLE stg_image (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_blob LONGBLOB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    coordinates VARCHAR(255) NULL
);