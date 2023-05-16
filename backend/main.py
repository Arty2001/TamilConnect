
import os
from flask import Flask, flash, request,render_template, Response, redirect, url_for, session
from flask_cors import CORS, cross_origin
from findRestobyGroceries import globalFunction
from findRecipesbyGroceries import findRecipesbyGroceries
from flask_session import Session


app = Flask(__name__, template_folder="../frontend/build", static_folder="../frontend/build/static")
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/') # creating website
@cross_origin()
def index():
    session["groceries"] = {"banana": False, "apple":False}
    return render_template('index.html')

@app.route('/api/FindResto')
@cross_origin()
def findResto():
    grocery=request.args.get("grocery")
    return globalFunction(grocery)

@app.route('/api/GetRecipes')
@cross_origin()
def getRecipes():
    return findRecipesbyGroceries()

@app.route('/api/groceries',methods=['GET', 'POST','DELETE'])
@cross_origin()
def addGroceries():
    if request.method == 'POST':
        grocery=request.args.get("grocery")
        session["groceries"][grocery]=True
        return "Submitted"
    if request.method == 'GET':
        cart = request.args.get("cart") 
        list_return = []
        for grocery in session["groceries"]:
            if cart == "True": 
                if session["groceries"][grocery] == True:
                    list_return.append(grocery)
            elif cart == "False":
                if session["groceries"][grocery] == False:
                    list_return.append(grocery)
        return list_return
    if request.method == 'DELETE':
        grocery=request.args.get("grocery")
        session["groceries"][grocery]=False
        return "Submitted"


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)

CORS(app, expose_headers='Authorization')