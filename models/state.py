#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', cascade="all,delete,delete-orphan",
        backref=backref('state', cascade='all, delete'),
        passive_deletes=True, single_parent=True)
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Give the City instances depending on the current State

            Returns:
                [list]: List of City instances with state_id equals to the current State.id
            """
            from models import storage
            from models.city import City
            cities_ls = []
            for key, value in storage.all(City):
                if value.state_id == self.id:
                    cities_ls.append(value)
            return cities_ls
