import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")
    

    def to_dict(self):
        return {}


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    firstname = Column(String(15), nullable=False)
    lastname = Column(String(15), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(15), unique=True, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email           
        }

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(28), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name           
        }
    
    def getAllPeople():
        all_people = People.query.all()
        all_people = list(map(lambda x: x.serialize(), all_people))
        return all_people
    
    def getPerson(id):
        person = People.query.get(id)
        return person.serialize()


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(28), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name           
        }
    def getAllPlanets():
        all_planets = Planets.query.all()
        all_planets = list(map(lambda x: x.serialize(), all_planets))
        return all_planets


class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(28), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title           
        }
    def getAllFilms():
        all_films = Films.query.all()
        all_films = list(map(lambda x: x.serialize(), all_films))
        return all_films


render_er(Base, 'diagram.png')
