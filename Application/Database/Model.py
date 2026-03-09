from sqlalchemy import Column, Integer, String
from Database import Base

class User(Base):
    __tablename__ = "UserDetail" #MySQL table 
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
