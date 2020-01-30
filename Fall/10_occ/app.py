
# Jionghao Wu
# SoftDev1 pd2
# K #10: Jinja Tuning
# 2019-09-23
from flask import Flask, render_template
import csv
import random
app = Flask(__name__)


@app.route("/")
def hello_world():
    print(__name__)
    return "no hablo queso!"

##coll = [0,1,1,2,3,5,8]
##
##@app.route("/templates/my_foist_template.html")
##def test_tmplt():
##    return render_template(
##        'my_foist_template.html',
##        foo="foooo",
##        collection=coll
##        )

occupations = {}
jobClass = []
percentage = []

@app.route("/occupyflaskst")
def occupy_flask_st():
    occupations = return_occupations()#gets dictionary of occupation.cvs
    randjob = randomOccupation()#gets random job
    for x in occupations:
        occupations[x] = str(occupations[x])
    return render_template("my_foist_template.html", randomOccupation = randjob, occupationsDict = occupations)



def return_occupations():
    with open( "./data/occupations.csv") as csv_file: #csv to dictionary
        csv_reader = csv.reader( csv_file, delimiter = ",")
        for row in csv_reader:
            occupations[ row[0]] = row[1]
        del occupations["Job Class"] #delete header
        del occupations["Total"] #delete footer
    return occupations

def randomOccupation(): 
    for occupation in occupations:
        jobClass.append(occupation)#adding to seperate lists
        percentage.append( float( occupations[ occupation]))#adding to seperate lists #percentage should be float
    return random.choices( jobClass, weights = percentage, k = 1)#picking random job

if __name__ == "__main__":
    app.debug = True
    app.run()
