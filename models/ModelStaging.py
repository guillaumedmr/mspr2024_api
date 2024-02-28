from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, LargeBinary, TIMESTAMP, VARCHAR

from extensions import db

class StgImage(db.Model):
    __bind_key__ = 'staging'  
    id = Column(Integer, primary_key=True, autoincrement=True)
    image_blob = Column(LargeBinary, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=db.func.now())
    coordinates = Column(VARCHAR(255))
    user = Column(VARCHAR(255), nullable=False)
