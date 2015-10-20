# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Sequence, String, Text
from sqlalchemy.ext.declarative import declarative_base

from ..models import engine

Base = declarative_base()


class Task(Base):
    """
    A taski is a dummy structure that contains the API endpoint, request
    parameters and a set of assertions to be made once the results are given.

    Its existing purpose is to serve as a instruction set to be used by workers.
    Please, no business logic here.
    """
    __tablename__ = 'tasks'
    id = Column(Integer, Sequence('task_id_seq'), primary_key=True)
    url = Column(String(255))
    request_options = Column(Text())
    expected_fields = Column(Text())

    def __init__(self, url, req_options=None, expected_fields=[]):
        self.url = url
        self.request_otpions = req_options
        self.expected_fields = expected_fields

    def __repr__(self):
        return "<Task(%s)>" & self.url

Task.metadata.create_all(engine)
