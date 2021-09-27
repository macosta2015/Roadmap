from flask import Flask

#APP INSTANCE: Refer to a singular version of something. 
#Variables with underscores before and after them are called magic methods
app = Flask(__name__) 
@app.route('/')
#Slash is known as the highest level of hierarchy in any computer system
def hello_world():
    return "Hello world"


if __name__ == '__main__': 
   app.run(port=5000, debug=True) # application will start listening for web request on port 5000

#Got it from Stackoverflorw
#app.run()

#This is the command that needs to be run in a mac in order to run with Flask
#export FLASK_APP=app.py


