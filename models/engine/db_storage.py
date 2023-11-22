#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import sys
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models in SQL format"""
    __engine = None
    __session = None
    reviews = relationship("Review", backref="place", cascade="all, delete")
    

    def __init__(self):
        '''init fun'''
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)
        Session = sessionmaker(self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        '''def all
        '''
        objs = {}
        if cls:
            for obj in self.__session.query(cls).all():
                objs[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in Base.__subclasses__():
                for obj in self.__session.query(cls).all():
                    objs[obj.__class__.__name__ + '.' + obj.id] = obj
        return objs

    def new(self, obj):
        '''def new'''
        self.__session.add(obj)

    def save(self):
        '''save'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete fun'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''reload func'''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
