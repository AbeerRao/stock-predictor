from flask import Flask, render_template, request, redirect, url_for, flash, Response
import json


app = Flask(__name__)

@app.route("/")
def index():
     data = []
     with open("data.json", "r") as f:
          data = json.load(f)
     return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)