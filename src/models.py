import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

 Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}





class StarWars (Base):
    __tablename__ = 'starwars'

    user = Column(String(250), nullable=False)
    planet = Column(String(250), nullable=False)
    charecter = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'user'
 
    user = Column(String(250), nullable=False)
    favorties = Column(String(250))
    starwars_user = Column(String(250), ForeignKey('starwars.user'))
    person = relationship(StarWars)


    class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    planet_name = Column(String(250), nullable=False)
    population = 


        class Charecter(Base):
    __tablename__ = 'charecter'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    charecters = Column(String(250), nullable=False)
    charecter_name = Column(String(250), nullable=False)
    planet_found = Column(String(250), nullable=False)


    def to_dict(self):
        return {}





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')