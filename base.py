# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy Engine que interage com o banco de dados PostgreSQL
engine = create_engine('postgresql://postgres:pass@172.17.0.2:5432/sqlalchemy_tutorial')
# Fábrica de sessões SQLAlchemy ORM vinculada ao Engine
Session = sessionmaker(bind=engine)

