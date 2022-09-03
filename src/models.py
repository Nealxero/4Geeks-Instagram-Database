import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(Integer, nullable=False)
    phone_number = Column(Integer, nullable=False)

    def to_dict(self):
        return {}

class Followers(Base):
    __tablename__ = 'Followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('User.id'))
    followers_id = Column(Integer, ForeignKey('Followers.id'))
   
    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=False)
    upload_Date = Column(String(250), nullable=False)
    Likes = Column(Integer, nullable=False)
    comments = Column(String(250), nullable=False) #Change to ID Later

    def to_dict(self):
        return {}

class Comments(Base):
    __tablename__ = 'Comments'
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    upload_Date = Column(String(250), nullable=False)