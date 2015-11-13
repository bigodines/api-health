# -*- coding: utf-8 -*-
import datetime
from wtforms_alchemy import ModelForm
from sqlalchemy import Column, Integer, String, Text, DateTime

from api_health.models.base import Base, engine


class Task(Base):
    """
    A simple model to encapsulate
    the domain of a Task. (Should be as dummy as possible)
    """
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    expected_fields = Column(Text)
    last_run = Column(DateTime)
    status = Column(String)

    def to_json(self):
        """Serializes a Task to JSON format"""
        return dict(id=self.id,
                    url=self.url,
                    expected_fields=self.expected_fields,
                    last_run=self.last_run,
                    status=self.status)

    def __repr__(self):
        return "<Task(id=%s, url=%s)>" % (self.id, self.url)


class TaskForm(ModelForm):
    class Meta:
        model = Task

# Initialize database schema (create tables)
Base.metadata.create_all(engine)
