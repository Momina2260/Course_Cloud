from sqlalchemy import Column,Integer,String,Text
from .database import Base,engine

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    password = Column(Text)
    gender  =  Column(String(50))
    role = Column(String(50))  
    #_____________________
class Course(Base):
    __tablename__="courses"
    id = Column(Integer,primary_key=True)
    title = Column(String(50))
    author = Column(String(50))
    description = Column(Text)
    