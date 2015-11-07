# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, DateTime, func

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
    last_run = Column(DateTime, default=func.now())
    status = Column(String)

    def __init__(self, url, expected_fields=None, status=None):
        self.url = url
        self.expected_fields = expected_fields
        self.status = status if status else 'FAIL'

    def __repr__(self):
        return "<Task(id=%s, url=%s)>" % (self.id, self.url)

# Initialize database schema (create tables)
Base.metadata.create_all(engine)
