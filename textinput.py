from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/foo.html")
def test_tmplt():
	print(app)
    return render_template('input.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
