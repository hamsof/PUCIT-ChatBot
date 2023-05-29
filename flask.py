#create a flask app that use pickled file to make a output
from flask import Flask,request,render_template
import pickle
app = Flask(__name__)
#load the pickled file
with open('py.pkl', 'rb') as file:
    function_serializer = pickle.load(file)
#make a route to the function
@app.route('/')
def hello_world():
    return render_template('index.html')