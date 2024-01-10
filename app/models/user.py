from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
    CreatedAt = Column(DateTime, default=datetime.now)

    # Relationships
    recipes = relationship('Recipe', back_populates='user')


    