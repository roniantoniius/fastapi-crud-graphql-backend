# to create a database connection and session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./marine_product.db"
db_engine     = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLokal = sessionmaker(bind=db_engine, autoflush=False, autocommit=False)
Base          = declarative_base()

