#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
from models.review import Review
>>>>>>> a58bc570ae84b96a13ec68ff845a4782023840bd
from models.place import Place
from models.review import Review

>>>>>>> e5aaa9d07724893244392feca44fc8071e4991e5

class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
<<<<<<< HEAD
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
=======
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
<<<<<<< HEAD
    places = relationship('Place', backref='user', cascade='all, delete')
    reviews = relationship('Review', backref='user', cascade='all, delete')
=======
    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")
>>>>>>> e5aaa9d07724893244392feca44fc8071e4991e5
>>>>>>> a58bc570ae84b96a13ec68ff845a4782023840bd
