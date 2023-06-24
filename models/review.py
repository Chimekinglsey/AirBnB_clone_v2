#!/usr/bin/python3
<<<<<<< HEAD
"""This is the review class"""
from sqlalchemy.ext.declarative import declarative_base
=======
""" Review module for the HBNB project """
<<<<<<< HEAD
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
=======
>>>>>>> a58bc570ae84b96a13ec68ff845a4782023840bd
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

>>>>>>> e5aaa9d07724893244392feca44fc8071e4991e5

class Review(BaseModel, Base):
<<<<<<< HEAD
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
=======
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
>>>>>>> a58bc570ae84b96a13ec68ff845a4782023840bd
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
<<<<<<< HEAD
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
=======
>>>>>>> e5aaa9d07724893244392feca44fc8071e4991e5
>>>>>>> a58bc570ae84b96a13ec68ff845a4782023840bd
