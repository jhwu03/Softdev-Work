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
    occupations = return_occupations()
    randjob = randomOccupation()
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
        jobClass.append(occupation)
        percentage.append( float( occupations[ occupation])) #percentage should be float
    return random.choices( jobClass, weights = percentage, k = 1)

if __name__ == "__main__":
    app.debug = True
    app.run()
