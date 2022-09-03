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
        return {
            "username":self.username
            }

class Followers(Base):
    __tablename__ = 'Followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('User.id'))
    followers_id = Column(Integer, ForeignKey('Followers.id'))
   
    def to_dict(self):
        return {
            "followers":self.followers_id
        }

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=False)
    upload_Date = Column(String(250), nullable=False)
    likes = Column(Integer, nullable=False)
    comments = Column(String(250), nullable=False) #Change to ID Later

    def to_dict(self):
        return {
            "description":self.description,
            "upload_Date":self.upload_Date,
            "likes":self.likes,
            "comments":self.comments
        }

class Comments(Base):
    __tablename__ = 'Comments'
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    upload_Date = Column(String(250), nullable=False)

    def to_dict(self):
        return {
            "comment":self.content,
            "upload_date":self.upload_Date
        }
#I Cant Generate the Diagram i dont know why 

render_er(Base, 'diagram.png')