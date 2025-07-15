import os
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String, default="В работе")
    brief = Column(String)
    client_id = Column(Integer)
    editors = Column(JSON)  # список ID
    producer_id = Column(Integer)

engine = create_engine(os.getenv("DATABASE_URL"))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
