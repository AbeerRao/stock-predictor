from flask import Flask, render_template, request, redirect, url_for, flash, Response


app = Flask(__name__)

@app.route("/")
def index():
     data = []
     with open("data.json", "r") as f:
          for i in f.readlines():
               data.append(i)
     return render_template("index.html", data=data[0])

if __name__ == "__main__":
    app.run(debug=True)