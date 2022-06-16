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
     def getHW():
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM hard_ware"

        mycursor.execute(sql)

        data = mycursor.fetchall()
        
        mycursor.close()

        mydb.close()

        return data

     def getHWByID(id):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM hard_ware WHERE id = {}".format(id)

        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

     def insertHW(name, hw_name):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "INSERT INTO hard_ware (name, hw_name, status, value) VALUES ('{}', '{}','OFF',0.00)".format(name, hw_name)

        mycursor.execute(sql)

        mydb.commit()

        ID = mycursor.lastrowid
        
        mycursor.close()

        mydb.close()
        

        return ID

     def updateStatusHW(ID, status):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE hard_ware SET status = '{}' WHERE id = {}".format(status, ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True

     def updateValueHW(ID, value):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE hard_ware SET value = {} WHERE id = {}".format(value, ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True

     def DeleteHW(ID):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "DELETE FROM hard_ware WHERE id = {}".format(ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True
    
