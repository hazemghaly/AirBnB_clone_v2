#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Getter attribute for City instances with matching state_id."""
        city_instances = storage.all(City)
        st_cities = [
            city for city in city_instances.values(
            ) if city.state_id == self.id]
        return st_cities
