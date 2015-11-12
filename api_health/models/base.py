from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api_health import settings

import os

engine = create_engine(settings.db_engine_url)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
