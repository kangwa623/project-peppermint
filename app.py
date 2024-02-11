# file: app.py

# Importing the necessary libraries and Flask boilerplate
from flask import Flask, render_template, url_for, redirect, jsonify

app = Flask(__name__)
app.static_folder = "static"




@app.route("/")
def Index():
    return render_template("index.html")

@app.route("/gallery")
def Gallery():
    return render_template("gallery.html")

@app.route("/echo")
def Echo():
    return render_template("echo.html")




if __name__ == '__main__':
    app.run(debug=True)