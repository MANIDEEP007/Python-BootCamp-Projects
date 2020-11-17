import sqlite3

#Function to connect to DB
def connect():
    #Connect to database
    conn = sqlite3.connect("routine.db")
    #Create Cursor Object
    cur = conn.cursor()
    #Create Table
    cur.execute('''CREATE TABLE IF NOT EXISTS routine(Id INTEGER PRIMARY KEY, Date TEXT,Earnings INTEGER, Exercise TEXT, Study TEXT, Diet TEXT, Python Text)''')
    #Commit The Changes
    conn.commit()
    #Close the connection
    conn.close()

def insert(date,earnings,exercise,study,diet,python):
    #Connect to database
    conn = sqlite3.connect("routine.db")
    #Create Cursor Object
    cur = conn.cursor()
    #Insert record into Table
    cur.execute('''INSERT INTO routine VALUES(NULL,?,?,?,?,?,?)''',(date,earnings,exercise,study,diet,python))
    #Commit The Changes
    conn.commit()
    #Close the connection
    conn.close()

def view():
    #Connect to database
    conn = sqlite3.connect("routine.db")
    #Create Cursor Object
    cur = conn.cursor()
    #Get data
    cur.execute('''SELECT * FROM routine''')
    #Get Rows
    rows = cur.fetchall()
    #Commit The Changes
    conn.commit()
    #Close the connection
    conn.close()
    return rows

def delete(id):
    #Connect to database
    conn = sqlite3.connect("routine.db")
    #Create Cursor Object
    cur = conn.cursor()
    #Delete data
    cur.execute('''DELETE FROM routine WHERE Id=?''',(id,))
    #Commit The Changes
    conn.commit()
    #Close the connection
    conn.close()

def search(date="",earnings="",exercise="",study="",diet="",python=""):
    #Connect to database
    conn = sqlite3.connect("routine.db")
    #Create Cursor Object
    cur = conn.cursor()
    #Get data
    cur.execute('''SELECT * FROM routine WHERE Date=? OR Earnings=? OR Exercise=? OR Study=? OR Diet=? OR Python=?''',(date,earnings,exercise,study,diet,python))
    #Get Rows
    rows = cur.fetchall()
    #Commit The Changes
    conn.commit()
    #Close the connection
    conn.close()
    return rows

connect()
