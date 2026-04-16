# import flask
from flask import *
# importing pymysql
import pymysql
import pymysql.cursors
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import secrets

# initializing the flask app
app = Flask(__name__)

import os
app.config["UPLOAD_FOLDER"] = 'static/images'

# Sign up api
# creating the route that corresponds to the web application function
@app.route("/api/signup", methods =["POST"])
# corresponding web application function
def signup():
    # get user input from user request
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    phone = request.form['phone']

    # Hash the password
    hashed_password = generate_password_hash(password)

    # creating a connection to the database
    connection = pymysql.connect(host= 'localhost', user = 'root', password = '', database = 'ecoshop')
    # defining the cursor
    cursor = connection.cursor()
    # defining the sql to insert data
    sql = "insert into users (username, password, email, phone) values (%s, %s, %s, %s)"
    # defining our data that will replace the placeholders in sql
    data = (username, hashed_password, email, phone)
    # execute the query
    cursor.execute(sql, data)
    # we need to commit to save the changes in the database
    connection.commit()
    # return a message to the user to show signup was successful
    return jsonify ({"Success" : "Thank you for signing up"})

# creating the route
@app.route("/api/signin", methods=['POST'])
def signin():
    # get user input
    email = request.form["email"]
    password = request.form["password"]

    # connect to database
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='ecoshop',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()

    # get user by email ONLY
    sql = "SELECT * FROM users WHERE email = %s"
    cursor.execute(sql, (email,))
    user = cursor.fetchone()

    # check if user exists AND password matches
    if user and check_password_hash(user["password"], password):
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user["id"],
                "username": user["username"],
                "email": user["email"],
                "phone": user["phone"]
            }
        })
    else:
        return jsonify({"message": "Login failed"})


# Social logins part
@app.route("/api/social-login", methods=["POST"])
def social_login():
    username = request.form["username"]
    email = request.form["email"]

    # connect to database
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='ecoshop'
    )
    cursor = connection.cursor()

    # check if user already exists
    sql = "SELECT * FROM users WHERE email = %s"
    cursor.execute(sql, (email,))
    user = cursor.fetchone()

    if user:
        return jsonify({"message": "Login successful"})
    else:
        # create new user (no password for social login)
        sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cursor.execute(sql, (username, email))
        connection.commit()

        return jsonify({"message": "User created via social login"})    





# add_product API
# creating the route
@app.route("/api/add_product", methods = ['POST'])
# defining the corresponding web application function
def add_product ():
    # getting the user input
    item_name = request.form ['item_name']
    item_description = request.form['item_description']
    item_cost = request.form['item_cost']
    photo = request.files['item_photo']
    
    # get the image file name
    filename = photo.filename
    # specify where the image will be stored
    photo_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
    # saving the photo
    photo.save(photo_path)


    # connecting to the database
    connection = pymysql.connect(host = 'localhost', user = 'root', password='', database='ecoshop')
    # defining the cursor
    cursor = connection.cursor()
    # crete the sql query
    sql = "insert into product_details (product_name, product_description, product_cost, product_photo) values(%s,%s,%s,%s)"
    # preaparing/defining the data for the sql query
    data = (item_name, item_description, item_cost,filename)
    # execute the query
    cursor.execute(sql, data)
    # commit/save the changes to the database
    connection.commit()
    # returning a response to the user
    return jsonify({"message" : "Product details added successfully"})

# get products API
# creating the route
@app.route("/api/get_items_details", methods = ['GET'])
# defining the corresponding web application function
def get_items_details():
    # connecting to the database
    connection = pymysql.connect(host = 'localhost', user = 'root', password='', database='ecoshop')
    # defining the cursor
    cursor = connection.cursor()
    # creating the SQL query
    sql = "SELECT * FROM product_details"
    # executing the query
    cursor.execute(sql)
    # fetching all the data from the database 
    items_details = cursor.fetchall()
    # closing the database connection
    connection.close()
    # returning the data to the user
    return jsonify( items_details)
# Social logins part
@app.route("/api/social-login", methods=["POST"])
def social_login():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    provider = data.get("provider")       # e.g. "google"
    provider_id = data.get("provider_id") # unique ID from provider

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='ecoshop'
    )
    cursor = connection.cursor()

    # Check if user exists
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()

    if user:
        # Optional: link provider if not already linked
        cursor.execute("""
            UPDATE users 
            SET provider=%s, provider_id=%s 
            WHERE email=%s
        """, (provider, provider_id, email))
        connection.commit()

        return jsonify({"message": "Login successful"})
    else:
        # Create new user
        cursor.execute("""
            INSERT INTO users (username, email, provider, provider_id)
            VALUES (%s, %s, %s, %s)
        """, (username, email, provider, provider_id))

        connection.commit()

        return jsonify({"message": "User created via social login"})



# run the app
app.run(debug= True)