import requests


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
     responseTF = response["prices"][: timeFrame]
     for rtf in responseTF:
          if 'type' in rtf:
               pass
          else:
               print(f"Date: {rtf['date']}\tOpening Price: {rtf['open']}\tClosing Price: {rtf['close']}")


if __name__ == '__main__':
     getUserInput()