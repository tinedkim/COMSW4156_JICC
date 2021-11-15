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

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=3000)
