<<<<<<< HEAD
'''
Begin server at 3000 and expose endpoints
'''

from flask import Flask, render_template, request, redirect, jsonify
from json import dump
from sqlalchemy import *
from sqlalchemy.pool import NullPool
app = Flask(__name__)

import os
import random
import time

DATABASEURI = os.environ.get("database-uri")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#get dining hall menu items
@app.route('/<hallID>', methods=['POST'])
def getDiningMenuItems(hallID):
    pass

#Login Page
@app.route('/login')
def login():
    return "<p>Login here</p>"

#Signup Page
@app.route('/signup')
def signup():
    return "<p>Sign up here</p>"
=======

@app.route("/topMenuItems")
def getTopMenuItems():
    queryName = "topMenuItems"
    return {queryName: []}

@app.route("/topDiningHalls")
def getTopDiningHalls():
    queryName = "topDiningHalls"
    return {queryName: []}

@app.route("/getUserHistory")
def getUserHistory():
    queryName = "getUserHistory"
    return {queryName: []}

@app.route("/getFoodReviews/:foodId")
def getFoodReviews():
    queryName = "foodReviews"
    return {queryName: []}

@app.route("/")
def landingPage():
    queryName = "CULFA"
    return "CULFA"
>>>>>>> ce8be250758cd84802f5bad62bd002c766bab0f9

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=3000)
