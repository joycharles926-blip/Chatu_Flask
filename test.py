# importing flask 
from flask import * 

# initializing and creating the flask app
app = Flask(__name__)

# defining a simple route/endpoint 
# the designated route in a web application that corresponds to a function
@app.route("/api/home")
# the web application function
def home():
    return jsonify ({"message" : "Welcome to home api"})





# defining a simple route/endpoint
@app.route("/api/products")
# defining corresponding web application function
def products():
    return jsonify ({"message" : "WElcome to the products api"})



# defining a simple route
@app.route("/api/services")
# defining the web function
def services():
    return jsonify ({"message": "Welcome to the services api"})



# run the app
app.run( debug= True) 