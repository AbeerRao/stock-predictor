import requests
import json
import datetime


def getUserInput():
     symbol = input("Enter the company symbol: ")
     timeFrame = int(input("Enter the time frame: "))
     getResponse(symbol, timeFrame)


def getResponse(symbol, timeFrame):
     url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"
     querystring = {"symbol": symbol, "region":"US"}
     headers = {
     'x-rapidapi-key': "b0eeaa196cmshce7e787214a081cp1e2eeejsnad2ccc22d7bb",
     'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
     }
     response = requests.request("GET", url, headers=headers, params=querystring).json()
     responseTF = response["prices"][ : timeFrame]
     responseFinal = []
     for rtf in responseTF:
          if 'open' not in rtf:
               pass
          else:
               rtf['date'] = datetime.datetime.fromtimestamp(rtf['date']).strftime('%Y-%m-%d')
               print(rtf['date'])
               responseFinal.append(rtf)
     responseFinalFinal = json.dumps(responseFinal)
     with open("data.json", "w") as f:
          f.write(responseFinalFinal)


if __name__ == '__main__':
     getUserInput()