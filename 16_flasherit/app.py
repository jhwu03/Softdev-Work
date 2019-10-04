#Team Hotpot huangT wuJh
#Tyler Huang
#SoftDev1 pd2
#K16: Oh yes, perhaps I do…
#2019-10-04

from flask import Flask, render_template, request, session, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = "bob123"

login = {'user': 'Bob', 'pass': '123'}
session = {}

@app.route("/")
def root():
    if 'user' in session: #if a user is already logged in then load the welcome page
        return render_template(
            "welcome.html",
            user = session['user'],
            )
    else: #else load the home page
        return render_template(
            "landingpage.html"
        )

@app.route("/auth", methods = ["POST"])
def authenticate():
    if (request.form['username'] != login['user'] or request.form['password'] != login['pass']): #if  neither the username nor password is correct
        errMsg = getErrorMsg() #get the error message
        flash("ERROR!")
        flash(errMsg)
        return redirect(url_for("error")) #redirect to the link given by the error method, which is the error page
    else:
        session['user'] = request.form['username'] #create new session and store the username
        flash("Congratulations! Login Success!")
        return render_template( #load the welcome page
            "welcome.html",
            user = request.form['username'],
        )

@app.route("/logout")
def logout(): #logs the user out from the welcome page
    session.pop('user', None); #remove the user from session
    return redirect(url_for("root")) #load the url for the root method which is the home page

@app.route("/error")
def error(): #loads the error page
    return render_template(
        "errorpage.html"
    )

@app.route("/return")
def returnPage(): #returns to the home page from error page
    return redirect(url_for("root")) #loads url for root method which is the home page

def getErrorMsg(): #gets the error message
    if (request.form['username'] != login['user'] and request.form['password'] != login['pass']): #if incorrect username and password
        return "Incorrect username and password. Please go back and try again."
    if (request.form['username'] != login['user']): #if incorrect username
        return "Incorrect username. Please go back and try again."
    if (request.form['password'] != login['pass']): #if incorrect password
        return "Incorrect password. Please go back and try again."

if __name__ == "__main__":
    app.debug = True
    app.run()
