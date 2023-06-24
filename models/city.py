#!/usr/bin/python3
"""This is the city class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
<<<<<<< HEAD
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
=======
<<<<<<< HEAD
    places = relationship("Place", backref='cities', cascade='all, delete')
    # name = ""
    # state_id = ''
=======
    places = relationship("Place", backref="cities", cascade="all, delete")
>>>>>>> e5aaa9d07724893244392feca44fc8071e4991e5
>>>>>>> a58bc570ae84b96a13ec68ff845a4782023840bd
