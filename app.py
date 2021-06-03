from flask import Flask, render_template, request, redirect, url_for, flash, Response
import json
import requests
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def result():
     if request.method == "POST":
          symbol = request.form["symbol"]
          timeFrame = request.form["time"]
          url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"
          querystring = {"symbol": symbol, "region":"US"}
          headers = {
          'x-rapidapi-key': "b0eeaa196cmshce7e787214a081cp1e2eeejsnad2ccc22d7bb",
          'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
          }
          response = requests.request("GET", url, headers=headers, params=querystring).json()
          responseTF = response["prices"][:int(timeFrame)]
          responseFinal = []
          for rtf in responseTF:
               if 'open' not in rtf:
                    pass
               else:
                    rtf['date'] = datetime.datetime.fromtimestamp(rtf['date']).strftime('%Y-%m-%d')
                    responseFinal.append(rtf)
          responseFinalFinal = json.dumps(responseFinal)
          with open("data.json", "w") as f:
               f.write(responseFinalFinal)
          data = []
          with open("data.json", "r") as f:
               data = json.load(f)
          return render_template("results.html", data=data)
     elif request.method == "GET":
          return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)