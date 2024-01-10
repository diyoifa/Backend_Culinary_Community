from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    content = Column(String(250))
    CreatedAt = Column(DateTime, default=datetime.now)

    # Relationships
    user = relationship('User')
    recipe = relationship('Recipe', back_populates='comments')