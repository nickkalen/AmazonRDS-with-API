#!/usr/bin/env python3

import os
import requests
import json
from twisted.internet import task, reactor
import mysql.connector

#create a function to insert api request into sql table
def insert_varibles_into_table(a, b, c):
        #set up database connection
        connection = mysql.connector.connect(host='ds3002-project2.c49pmqg9usnv.us-east-1.rds.amazonaws.com',
                                             database='project2',
                                             user='ds3002',
                                             password=os.environ.get("RDS_PASS"))
                                             
        #set up the cursor and write the sql statement to insert the 3 parameters into the apidata table                                    
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO apidata (factor, pi, time) 
                                VALUES (%s, %s, %s) """
        record = (a, b, c)
        #execute the sql statement to insert the 3 params in sql table
        cursor.execute(mySql_insert_query, record)
        connection.commit()

#function that pulls from the api then appends the data to the apidata table
def doWork():
    response = requests.get(url='https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi')
    data = response.json()
    insert_varibles_into_table(data["factor"], data["pi"], data["time"])
    pass

#once the reactor starts, the doWork() function will execute every 60 seconds
l = task.LoopingCall(doWork)
l.start(60.0)  #call every sixty seconds

#makes sure reactor stops after 59 minutes, ensuring we have 60 rows of data
reactor.callLater(60*59, reactor.stop)
#starts the reactor
reactor.run()

