from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, schema
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:////tmp/test.db')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
