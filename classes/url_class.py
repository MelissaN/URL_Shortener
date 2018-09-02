#!/usr/bin/python3
"""
Class URL
"""
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class URL(Base):
    """Class URL is a blueprint to create url objects"""

    __tablename__ = "long_short_urls"

    short_url = Column(String(255), nullable=False, primary_key=True)
    long_url = Column(String(255), nullable=False)

    def __init__(self, **kwargs):
        """Initialize instance attributes"""
        self.short_url = ""
        self.long_url = ""
        for k, v in kwargs.items():
            setattr(self, k, v)
