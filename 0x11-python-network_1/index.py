import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        print(json_data)
    else:
        print("request failed with status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error:", e)