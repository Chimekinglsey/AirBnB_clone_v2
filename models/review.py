#!/usr/bin/python3
""" Review module for the HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

>>>>>>> e5aaa9d07724893244392feca44fc8071e4991e5

class Review(BaseModel, Base):
    """ Review classto store review information """
<<<<<<< HEAD
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('place.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    
    """place_id = ""
    user_id = ""
    text = """""
=======
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
>>>>>>> e5aaa9d07724893244392feca44fc8071e4991e5
