#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv
from models.engine.db_storage import DBStorage

db = 'HBNB_MYSQL_DB'
ev = getenv('HBNB_TYPE_STORAGE')
if db == ev:
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
