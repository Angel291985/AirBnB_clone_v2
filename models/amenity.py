#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage_type
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """ The class represents the table name, amenities
    Attribute:
        name: represents column containing a string (128 characters)
    """
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
