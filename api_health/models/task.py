# -*- coding: utf-8 -*-
import datetime
from wtforms_alchemy import ModelForm
from sqlalchemy import Column, Integer, String, Text, DateTime, func

from api_health.models.base import Base, engine


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

    def __init__(self, url=None, expected_fields=None, status=None):
        self.url = url
        self.expected_fields = expected_fields
        self.status = status if status else 'FAIL'



class TaskForm(ModelForm):
    class Meta:
        model = Task

# Initialize database schema (create tables)
Base.metadata.create_all(engine)
