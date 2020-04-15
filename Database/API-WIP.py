"""
Routes and views for the flask application.
"""

from databaseORM import Program
from  databaseConfiguration import app
from flask import render_template,request, jsonify, Flask



#app = Flask(__name__)
app.config["DEBUG"] = True

#psuedo code from book for api
#might need to do one for each page,
#need to look more into this
#so we'll need one for the admin dash, admin login
#browse, and result
@app.route('/', methods=['GET'])
def home():
    proglist = []
    programs = Program.return_all_programs()
    for prog in programs:
        proglist.append(prog)
    
    return  jsonify(json_list = [i.serialize for i in proglist])

#checking verbs of incoming request
@app.route('/check', methods=['GET','POST', 'PUT', 'DELETE'])
def check():
    if request.method == GET:
        return "REQUEST TYPE: GET"
    elif request.method == POST:
        return "REQUEST TYPE: POST"
    elif request.method == PUT:
        return "REQUEST TYPE: PUT"
    elif request.method == DELETE:
        return "REQUEST TYPE: DELETE"


# A route to return all of the available entries in our catalog.
#@app.route('/api/v1/resources/books/all', methods=['GET'])
#def api_all():
#    return jsonify(books)

if True:
    app.run()

