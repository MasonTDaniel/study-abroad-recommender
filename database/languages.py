from db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


#Association Table refrences back to programs
programs_languages = Table('Programs_Languages', Base.metadata,
db.Column('program_id', db.Integer, ForeignKey('programs.id')),
db.Column('language_id', db.Integer, ForeignKey('languages.id')))


class Language(db.Model):

#Individual Attributes

	__tablename__ = "languages"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))


#Relationship 
	programs = relationship("Program", secondary=programs_languagess, back_populates="languages")


#Individual Methods

	#optional method to set the porper string representation of the object
	def __repr__(self):
		return "<Language(id='%d', name='%s')>" % (self.id, self.name)

	def __init__(self, name):
        	self.area_name = name

	def save_to_db(self):
        	db.session.add(self)
        	db.session.commit()


#Class Methods
	#This is where search methods will go. There is a reference of how to 
	# in the programs file