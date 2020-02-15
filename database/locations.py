from db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()




#Association table to programs.py
programs_cities = Table('Programs_Cities', Base.metadata,
	db.Column('program_id', db.Integer, ForeignKey('programs.id')),
	db.Column('city_id', db.Integer, ForeignKey('city.id')))




class City(db.Model):
	
#Individual Attributes
	__tablename__="city"
	
	id = db.Column(db.Integer, primary_key=True)
	city = db.Column(db.String(100))


#Relationships
	programs = relationship("Program", secondary=programs_cities, back_populates="program_city")
	country = relationship("Country", secondary=cities_countries, back_populates="cities")


#Individual Methods
	#optional method to set the porper string representation of the object
	def __repr__(self):
		return "<City(City ID='%d', Name='%s')>" % (self.id, self.name)

	def __init__(self, id, name):
        	self.id = id
        	self.city = name

	def save_to_db(self):
        	db.session.add(self)
        	db.session.commit()


#Class Methods
	#This is where search methods will go. There is a reference of how to 
	# in the programs file







#Association table 
cities_countries = Table('Cities_Countries', Base.metadata,
	db.Column('city_id', db.Integer, ForeignKey('city.id')),
	db.Column('country_id', db.Integer, ForeignKey('country.id')))








#This is the class to define the country table with ids
class Country(db.Model):

#Individual Attributes
	__tablename__ = "country"

	id = db.Column(db.Integer, primary_key=True)
	country = db.Column(db.String(100))


#Relationship
	cities = relationship("City", secondary=cities_countries, back_populates="country")


#Individual Methods
	#optional method to set the porper string representation of the object
	def __repr__(self):
		return "<Country(Country ID='%d', Name='%s')>" % (self.id, self.name)

	def __init__(self, id, name):
        	self.id = id
        	self.country = name
	def save_to_db(self):
        	db.session.add(self)
        	db.session.commit()


#Class Methods
	#This is where search methods will go. There is a reference of how to 
	# in the programs file