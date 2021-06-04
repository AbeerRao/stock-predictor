from flask import Flask, render_template, request, redirect, url_for, flash, Response
import json
import requests
import datetime
from sklearn.model_selection import train_test_split
import sklearn.svm
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
import pandas as pd

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
          dataset = pd.read_json("data.json")
          dataset = dataset.set_index(pd.DatetimeIndex(dataset['date'].values))
          dataset.index.name = 'date'
          dataset['price_up'] = np.where(dataset['close'].shift(-1) > dataset['close'], 1, 0)
          dataset = dataset.drop(columns=['date'])
          x = dataset.iloc[:, :dataset.shape[1]-1].values
          y = dataset.iloc[:, dataset.shape[1]-1].values
          x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
          sc = StandardScaler()
          x_train[:, :] = sc.fit_transform(x_train[:, :])
          x_test[:, :] = sc.transform(x_test[:, :])
          classifer = sklearn.svm.SVC(kernel = 'linear', random_state = 0)
          classifer.fit(x_train, y_train)
          y_pred = classifer.predict(x_test)
          cm = confusion_matrix(y_test, y_pred)
          ac = accuracy_score(y_test, y_pred)
          accuracy = "{percent:.2%}".format(percent=ac)
          pred_data = [y_pred[-1], cm, accuracy]
          return render_template("results.html", data=data, pred_data=pred_data)
     elif request.method == "GET":
          return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)