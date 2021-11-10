"""
Columbia's COMS W4111.001 Introduction to Databases
Example Webserver
To run locally:
    python server.py
Go to http://localhost:8111 in your browser.
A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""
import os
import random
import time
  # accessible as a variable in index.html:
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
#
# The following is a dummy URI that does not connect to a valid database. You will need to modify it to connect to your Part 2 database in order to use the data.
#
# XXX: The URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@34.73.36.248/project1
#
# For example, if you had username zy2431 and password 123123, then the following line would be:
#
#     DATABASEURI = "postgresql://zy2431:123123@34.73.36.248/project1"
#
DATABASEURI = "postgresql://cl3945:china_databases@34.73.36.248/project1" # Modify this with your own credentials you received from Joseph!
#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)
#
# Example of running queries in your database
# Note that this will probably not work if you already have a table named 'test' in your database, containing meaningful data. This is only an example showing you how to run queries in your database using SQLAlchemy.
#
engine.execute("""CREATE TABLE IF NOT EXISTS test (
  id serial,
  name text
);""")
engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")
@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request.
  The variable g is globally accessible.
  """
  try:
    g.conn = engine.connect()
  except:
    print("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass

@app.route('/<cust_id>/profile')
def profile(user_id):
    cursor = g.conn.execute('SELECT* FROM customer where custid = %s', user_id)
    for result in cursor:
        result = result

    return render_template("profile.html", result = result, user_id = user_id)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/check', methods = ['POST'])
def checkCredentials():
    name = request.form['name']
    email = request.form['email']
    cursor = g.conn.execute('SELECT userid FROM user WHERE name = %s and email = %s', name, email)
    custID = -1
    for result in cursor:
        custID = result[0]
    if custID == -1:
        return render_template("error.html")
    url = '/' + custID
    return redirect(url)

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/createuser', methods=['POST'])
def create_customer():
    name = request.form['name']
    email = request.form['email']
    cursor = g.conn.execute('SELECT COUNT(*) FROM user')
    for result in cursor:
        custid = int(result[0]) + 1
    try:
        cursor = g.conn.execute('INSERT INTO user(userid, name, email) VALUES (%s, %s, %s)', custid, name, email)
    except:
        return render_template("signuperror.html")
    url = '/' + str(custid)
    return redirect(url)

if __name__ == "__main__":
  import click
  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:
        python server.py
        
    Show the help text using:
        python server.py --help
    """
    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)
  run()
