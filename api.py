import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"

querystring = {"symbol":"AMRN","region":"US"}

headers = {
    'x-rapidapi-key': "b0eeaa196cmshce7e787214a081cp1e2eeejsnad2ccc22d7bb",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()

print(response["prices"])