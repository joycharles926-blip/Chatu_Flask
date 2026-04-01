# import flask
from flask import *

# importing pymysql
import pymysql
import pymysql.cursors
from flask_cors import CORS

# initializing the flask app
app = Flask(__name__)
CORS(app)

# importing os
import os

# creating a folder to save the images
app.config["UPLOAD_FOLDER"] = 'static/images'

# signup API
# creating the route that corresponds to the web application function
@app.route("/api/signup", methods =["POST"])
# corresponding web application function
def signup():
    # get user input from user request
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    phone = request.form['phone']

    # creating a connection to the database
    connection = pymysql.connect(host= 'localhost', user = 'root', password = '', database = 'chatusokogarden')
    # defining the cursor
    cursor = connection.cursor()
    # defining the sql to insert data
    sql = "insert into users (username, password, email, phone) values (%s, %s, %s, %s)"
    # defining our data that will replace the placeholders in sql
    data = (username, password, email, phone)
    # execute the query
    cursor.execute(sql, data)
    # we need to commit to save the changes in the database
    connection.commit()
    # return a message to the user to show signup was successful
    return jsonify ({"Success" : "Thank you for signing up"})

# signin API
# creating the route
@app.route("/api/signin", methods = ['POST'])
# Defining the corresponding function
def signin():
    # getting user input
    email = request.form["email"]
    password = request.form["password"]
    # creating a connection to the database
    connection = pymysql.connect(host='localhost', user='root', password='', database='chatusokogarden')
    # defining our cursor
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    # defining our sql query to select
    sql = "select * from users where email = %s and password = %s"
    # defining our data to replace the placeholders
    data = (email, password)
    # executing the query
    cursor.execute(sql,data)
    # creating conditions for when the rows are zero or more
    count = cursor.rowcount
    # condition for when the rows are zero
    if count ==0:
        return jsonify({"message" : "Login failed"})
    else:
        user=cursor.fetchone()
        return jsonify ({"message": "Login successful", "user":user})



# add_product API
# creating the route
@app.route("/api/add_product", methods = ['POST'])
# defining the corresponding web application function
def add_product ():
    # getting the user input
    product_name = request.form ['product_name']
    product_description = request.form['product_description']
    product_cost = request.form['product_cost']
    photo = request.files['product_photo']
    
    # get the image file name
    filename = photo.filename
    # specify where the image will be stored
    photo_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
    # saving the photo
    photo.save(photo_path)


    # connecting to the database
    connection = pymysql.connect(host = 'localhost', user = 'root', password='', database='chatusokogarden')
    # defining the cursor
    cursor = connection.cursor()
    # crete the sql query
    sql = "insert into product_details (product_name, product_description, product_cost, product_photo) values(%s,%s,%s,%s)"
    # preaparing/defining the data for the sql query
    data = (product_name, product_description, product_cost,filename)
    # execute the query
    cursor.execute(sql, data)
    # commit/save the changes to the database
    connection.commit()
    # returning a response to the user
    return jsonify({"message" : "Product details added successfully"})


# get_product_details API
# creating the route
@app.route("/api/get_product_details")
# define the corresponding web application function
def get_product_details():
    # establish a connection to the database
    connection = pymysql.connect(host= "localhost", user= "root", password= "", database= "chatusokogarden")
    # define the cursor
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    # defining the sql query
    sql = "select * from product_details"
    # executing the sql query
    cursor.execute(sql)
    # fetching all the rows returned after sql execution
    product_details = cursor.fetchall()
    # closing the database connection
    connection.close()
    # returning a response to the user
    return jsonify (product_details)



# Mpesa Payment Route/Endpoint 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    if request.method == 'POST':
        amount = request.form['amount']
        phone = request.form['phone']
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/api/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return jsonify({"message": "Please Complete Payment in Your Phone and we will deliver in minutes"})
    



# run the app
app.run(debug= True)