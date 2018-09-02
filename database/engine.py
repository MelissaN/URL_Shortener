#!/usr/bin/python3
"""
DATABASE ENGINE FOR STORAGE
"""
from classes.url_class import URL
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
Base = declarative_base()


class DBStorage():
    """
       database engine to store urls
    """
    __engine = None
    __session = None

    def __init__(self):
        """
           create engine and link to database
        """
        user="root"
        pw=""
        host="localhost"
        db="urlshort_dev_db"
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pw, host, db), pool_pre_ping=True)
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def save(self, obj):
        """
           create new obj and save entry to db
        """
        self.__session.add(obj)
        self.__session.commit()

    def all(self):
        """
           return all entries in db
        """
        url_dic = {}
        for obj in self.__session.query(URL).all():
            key = obj.short_url
            url_dic[key] = obj.long_url
        return url_dic

    def get(self, short_url):
        """
           return long_url if short_url given
        """
        try:
            obj = self.__session.query(URL).get(short_url)
            return obj.long_url
        except (IndexError, TypeError):
            return ""
