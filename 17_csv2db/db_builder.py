#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >


#command = "CREATE TABLE roster (name TEXT, userid INTEGER)"          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement
a = "bob"
command = "INSERT INTO roster VALUES (\"bob\", 20);"
c.execute(command)
command = "SELECT * FROM roster;"
c.execute(command)
print(c.fetchall())

#==========================================================

db.commit() #save changes
db.close()  #close database
