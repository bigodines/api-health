# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text

from .base import Base, engine


class Task(Base):
    """
    A simple model to encapsulate
    the domain of a Task. (Should be as dummy as possible)
    """
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    expected_fields = Column(Text)

    def __init__(self, url, expected_fields=None):
        self.url = url
        self.expected_fields = expected_fields

    def __repr__(self):
        return "<Task(id=%s, url=%s)>" % (self.id, self.url)

# Initialize database schema (create tables)
Base.metadata.create_all(engine)
