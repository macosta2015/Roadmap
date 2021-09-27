
import detetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflec=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)
@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

import app

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")






######################################################################################
#from flask import Flask

#APP INSTANCE: Refer to a singular version of something. 
#Variables with underscores before and after them are called magic methods
#app = Flask(__name__) 
#@app.route('/')
#Slash is known as the highest level of hierarchy in any computer system
#def hello_world():
#    return "Hello world"


#if __name__ == '__main__': 
#   app.run(port=5000, debug=True) # application will start listening for web request on port 5000

#Got it from Stackoverflorw
#app.run()

#This is the command that needs to be run in a mac in order to run with Flask
#export FLASK_APP=app.py


