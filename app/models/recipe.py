from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    Title = Column(String(50))
    Description = Column(String(250))
    Ingredients = Column(String(250))
    instructions = Column(String(250))
    cook_time = Column(String(50))
    difficulty = Column(String(50))
    image = Column(String(50))
    category = Column(String(50))
    CreatedAt = Column(DateTime, default=datetime.now)

    # Define la relación
    user = relationship('User', back_populates='recipes')
    likes = relationship('Like', back_populates='recipe')
    comments = relationship('Comment', back_populates='recipe')