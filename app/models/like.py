from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
# from ..internal.db import engine, meta_data


Base = declarative_base()

class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

    # Relationships
    user = relationship('User')
    recipe = relationship('Recipe', back_populates='likes')
