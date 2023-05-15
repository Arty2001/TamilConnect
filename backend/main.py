
import os
from flask import Flask, flash, request,render_template, Response, redirect, url_for, session
from flask_cors import CORS, cross_origin
from findRestobyGroceries import findRestobyGroceries
from findRecipesbyGroceries import findRecipesbyGroceries

app = Flask(__name__, template_folder="../frontend/build", static_folder="../frontend/build/static")

@app.route('/') # creating website
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/api/FindResto')
@cross_origin()
def findResto():
    grocery=request.args.get("grocery")
    return findRestobyGroceries(grocery)

@app.route('/api/GetRecipes')
@cross_origin()
def getRecipes():
    return findRecipesbyGroceries()

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', port=5000, threaded=True, use_reloader=False)

CORS(app, expose_headers='Authorization')