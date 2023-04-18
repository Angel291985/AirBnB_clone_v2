#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
# from models.place import place_amenity


class Amenity(BaseModel, Base):
    """ The class represents the table name, amenities
    Attribute:
        name: represents column containing a string (128 characters)
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    # place_amenities = relationship('Place', secondary='place_amenity')
