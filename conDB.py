import mysql.connector

def con():
    mydb = mysql.connector.connect(
    host="localhost",
    user="project",
    password="project",
    database="project"
    )
    return mydb

class Con:
    