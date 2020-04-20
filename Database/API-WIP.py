"""
Routes and views for the flask application.
"""

from databaseORM import Admin,areas,terms,locations,languages,programs,Program,Area,Term,Location,Language,Provider 
from  databaseConfiguration import app, db
from flask import render_template,request, jsonify, flask



#app = Flask(__name__)
app.config["DEBUG"] = True

#psuedo code from book for api
#might need to do one for each page,
#need to look more into this
#so we'll need one for the admin dash, admin login
#browse, and result
@app.route('/', methods=['GET'])
def home():
    programs = Program.return_all_programs()
    json_list=[i.serialize for i in programs]
    return  jsonify(json_list)


@app.route('/results', methods=['GET'])
def results():
    # the following values are taken from the get request and can be used to filter
    #if null, dont filter by it
    languageRequest = flask.request.values.get('lan')
    locationRequest = flask.request.values.get('loc')
    areaRequest = flask.request.values.get('area')
    termRequest = flask.request.values.get('term')
    providerRequest = flask.request.values.get('prov')

   
    filterResults = None
     # here should be the methods to filter





    #after results are gathered
    json_list = [i.serialize for i in filterResults]
    return jsonify(json_list)

    return 



#checking verbs of incoming request
@app.route('/admin', methods=['GET','POST', 'PUT', 'DELETE'])
def check():
    if request.method == GET:
        languageRequest = flask.request.values.get('lan')
        locationRequest = flask.request.values.get('loc')
        areaRequest = flask.request.values.get('area')
        termRequest = flask.request.values.get('term')
        providerRequest = flask.request.values.get('prov')

    
        filterResults = None
     # here should be the methods to filter





    #after results are gathered
        json_list = [i.serialize for i in filterResults]
        return jsonify(json_list)

    elif request.method == POST:
        #use post to update
        programID = flask.request.values.get('id')
        updateName = flask.request.values.get('uName')
        # each new update variable will be named and received in a simmilar fasion. It will look messy

        
        #find the program
        #modify the selected values with data given
        #update modified date
        # if the program is successfully modified 
            #return jsonify("success")
        #else, return either a message saying it failed or render the page with an error sent 

    elif request.method == PUT:

        # same as above, only it doesnt need to look up anything, just take in the values and use them to make a program. 
        #id not required, but the database should be checked to see if a program of the same name exists. 
        #if it does, do nothing and return an error
        return None
    elif request.method == DELETE:

        #given the id of a program, delete it from database
        programID= flask.request.values.get('id')
        return "REQUEST TYPE: DELETE"


# A route to return all of the available entries in our catalog.
#@app.route('/api/v1/resources/books/all', methods=['GET'])
#def api_all():
#    return jsonify(books)

if True:
    app.run()













#Below Contains code for the updating, removing, and adding information in the database
#This is a generic script to populate an entire new program
#   If a parameter is optional, then pass "None" for the value: cost, cost_stipulations, description, url (optional)
#   If it is meant to be a list, then leave the list empty "[]": areas, terms, languages, locations (optional)
def create_new_program(providerName, programName, com, res, intern, cost, cost_stipulations, description, url, areas, terms, languages, locations): 
    #-----------------------------PROVIDER RELATIONSHIP----------------------------
    # Check if the provider already exist, if it doesn't then make a new provider
    if(Provider.get_provider_id(providerName) == -1):
        prov = Provider(providerName)
        prov.save_to_db()
    else: 
        prov = Provider.find_by_name(providerName)

    # Check if the program already exist, if it doesn't then make a new program
    if(Program.get_program_id(programName) == -1):
        prog = Program(programName, com, res, intern, cost, cost_stipulations, description, url)
        prog.save_to_db()
    else: 
        prog = Program.find_by_name(programName)

    #Add the program to the provider
    prov.add_program(prog)
    prov.save_to_db()


    #-----------------------------PROGRAM RELATIONSHIPS----------------------------
    # AREA, TERM, LANGUAGES, LOCATION

    # AREA: 
    # Cyle through all area names: check to see if the area already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in areas:
        if(Area.get_area_id(i) == -1):
            tempArea = Area(i)
            tempArea.save_to_db()
        else: 
            tempArea = Area.find_by_name(i)
        
        prog.add_area(tempArea)
        prog.save_to_db()
        #might need save to db methods

    # TERM: 
    # Cyle through all term names: check to see if the term already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in terms:
        if(Term.get_term_id(i) == -1):
            tempTerm = Term(i)
            tempTerm.save_to_db()
        else: 
            tempTerm = Term.find_by_name(i)
        
        prog.add_term(tempTerm)
        prog.save_to_db()
        #might need save to db methods

    # LANGUAGES: 
    # Cyle through all term names: check to see if the term already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in languages:
        if(Language.get_language_id(i) == -1):
            tempLanguage = Language(i)
            tempLanguage.save_to_db()
        else: 
            tempLanguage = Language.find_by_name(i)
        
        prog.add_language(tempLanguage)
        prog.save_to_db()
        #might need save to db methods

    # LOCATION: 
    # Cyle through all term names: check to see if the term already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in locations:
        if(Location.get_location_id(i[0], i[1]) == -1):
            tempLocation = Location(i[0], i[1])
            tempLocation.save_to_db()
        else: 
            tempLocation = Location.find_by_name(i[0], i[1])
        
        prog.add_location(tempLocation)
        prog.save_to_db()





#This method will define changing or removing a term from a program
#   If it is removing, the front end will pass "remove"
#   If it is adding, the front end will pass "add" for first 
#Parameters: 
#   change- (string: "add" or "remove")  specify desired change to db
#   program- (string) name of program that the terms are being changed for
#   terms- (list) names of terms being added or removed from program
# Return True if completed
def add_or_remove_term(change, program, terms):
    
    prog = Program.find_by_name(programName)

    if(prog == None):
        raise ValueError
    if(terms == []):
        raise ValueError

    if(change == "add"):
        for i in terms:
            tempTerm = Term.find_by_name(i)

            if(tempTerm == None):
                tempTerm = Term(i)
                tempTerm.save_to_db()

            prog.add_term(tempTerm)
            prog.save_to_db()

    elif(change == "remove"):
        for i in terms:
            tempTerm = Term.find_by_name(i)

            if(tempTerm == None):
                raise ValueError

            prog.remove_term(tempTerm)
            prog.save_to_db()

            #This if statement checks to see if the removed Language has any more existing relationships
            #   If there are none, then delete the language from the database 
            if(Term.query.join(Programs_Terms).filter((Programs_Terms.c.term_id == tempTerm.id)).first() == None):
                tempLanguage.delete()

            prog.save_to_db()
    else:
        raise ValueError    #IF change is not "add" or "remove"

    session.commit()
    return True


#This method will define changing or removing a area from a program
#   If it is removing, the front end will pass "remove"
#   If it is adding, the front end will pass "add" for first 
#Parameters: 
#   change- (string: "add" or "remove")  specify desired change to db
#   program- (string) name of program that the areas are being changed for
#   areas- (list) names of areas being added or removed from program
# Return True if completed
def add_or_remove_area(change, program, areas):
    
    prog = Program.find_by_name(programName)

    if(prog == None):
        raise ValueError
    if(areas == []):
        raise ValueError

    if(change == "add"):
        for i in areas:
            tempArea = Area.find_by_name(i)

            if(tempArea == None):
                tempArea = Area(i)
                tempArea.save_to_db()

            prog.add_area(tempArea)
            prog.save_to_db()

    elif(change == "remove"):
        for i in areas:
            tempArea = Area.find_by_name(i)

            if(tempArea == None):
                raise ValueError

            prog.remove_area(tempArea)
            prog.save_to_db()

            #This if statement checks to see if the removed Language has any more existing relationships
            #   If there are none, then delete the language from the database 
            if(Areas.query.join(Programs_Areas).filter((Programs_Areas.c.area_id == tempArea.id)).first() == None):
                tempArea.delete()

            prog.save_to_db()
    else:
        raise ValueError

    session.commit()
    return True


#This method will define changing or removing a language from a program
#   If it is removing, the front end will pass "remove"
#   If it is adding, the front end will pass "add" for first 
#Parameters: 
#   change- (string: "add" or "remove")  specify desired change to db
#   program- (string) name of program that the languages are being changed for
#   languages- (list) names of languages being added or removed from program
# Return True if completed
def add_or_remove_language(change, program, languages):
    
    prog = Program.find_by_name(programName)

    if(prog == None):
        raise ValueError
    if(languages == []):
        raise ValueError

    if(change == "add"):
        for i in languages:
            tempLanguage = Language.find_by_name(i)

            if(tempLanguage == None):
                tempLanguage = Language(i)
                tempLanguage.save_to_db()

            prog.add_language(tempLanguage)
            prog.save_to_db()

    elif(change == "remove"):
        for i in languages:
            tempLanguage = Language.find_by_name(i)

            if(tempLanguage == None):
                raise ValueError

            prog.remove_language(tempLanguage)
            prog.save_to_db()

            #This if statement checks to see if the removed Language has any more existing relationships
            #   If there are none, then delete the language from the database 
            if(Languages.query.join(Programs_Languages).filter((Programs_Languages.c.language_id == tempLanguage.id)).first() == None):
                tempLanguage.delete()

            prog.save_to_db()
    else:
        raise ValueError

    session.commit()
    return True



#THIS NEEDS TO BE CHANGED TO ACCOMIDATE CITY AND COUNTRY

#This method will define changing or removing a location from a program
#   If it is removing, the front end will pass "remove"
#   If it is adding, the front end will pass "add" for first 
#Parameters: 
#   change- (string: "add" or "remove")  specify desired change to db
#   program- (string) name of program that the languages are being changed for
#   locations- (list) names of locations being added or removed from program
# Return True if completed
def change_or_remove_location(change, program, locations):
    
    prog = Program.find_by_name(programName)

    if(prog == None):
        raise ValueError
    if(locations == []):
        raise ValueError

    if(change == "add"):
        for i in locations:
            tempLocation = Location.find_by_name(i)

            if(tempLocation == None):
                tempLocation = Location(i)
                tempLocation.save_to_db()

            prog.add_location(tempLocation)
            prog.save_to_db()

    elif(change == "remove"):
        for i in locations:
            tempLocation = Location.find_by_name(i)

            if(tempLocation == None):
                raise ValueError

            prog.remove_location(tempLocation)
            prog.save_to_db()

            #This if statement checks to see if the removed Language has any more existing relationships
            #   If there are none, then delete the language from the database 
            if(Locations.query.join(Programs_Locations).filter((Programs_Locations.c.location_id == tempLocation.id)).first() == None):
                tempLocation.delete()

            prog.save_to_db()
    else:
        raise ValueError

    session.commit()
    return True



#Need to add provider and program add and remove method



#Refrences Used: 
# https://stackoverflow.com/questions/41270319/how-do-i-query-an-association-table-in-sqlalchemy