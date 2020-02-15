from db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()



#Association Table refrences back to programs
programs_terms = Table('Programs_Terms', Base.metadata,
	db.Column('program_id', db.Integer, ForeignKey('programs.id')),
	db.Column('term_id', db.Integer, ForeignKey('term.id')))




class Term(db.Model):
	
#Individual Attributes
	__tablename__ = "term"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(10))


#Relationship
	programs = relationship("Program", secondary=programs_terms, back_populates="program_term")


#Individual Methods

	#optional method to set the porper string representation of the object
	def __repr__(self):
		return "<Term(id='%d', name='%s')>" % (self.id, self.name)

	def __init__(self, name):
        	self.term_name = name

	def save_to_db(self):
        	db.session.add(self)
        	db.session.commit()


#Class Methods
	#This is where search methods will go. There is a reference of how to 
	# in the programs file