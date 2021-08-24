from sqlalchemy import Column, Integer, BigInteger, String, Float, ForeignKey, DateTime, Boolean
from database import Base
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from datetime import datetime



class User(Base):
    __tablename__ = 'user'
    email_id = Column(String(255), primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    phone_no = Column(String(255), nullable=False)
    created_time = Column(DateTime, nullable=False, default=datetime.now())
