from typing_extensions import Required
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DATETIME, FLOAT
from sqlalchemy.sql.sqltypes import Interval
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship

from api.dbutils.database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(128), unique=True)
    firstname = Column(String(64), nullable=True)
    lastname = Column(String(64), nullable=True)
    age = Column(String(3)) 
    nid = Column(String(10))    
    image = Column(String(128), nullable=True)
    # group = relationship("Groups", back_populates="user")