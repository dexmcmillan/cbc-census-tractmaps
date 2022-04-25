import pandas as pd
import requests
import json

CHART_ID = "WXIHo"

with open('./auth.txt', 'r') as f:
        DW_AUTH_TOKEN = f.read().strip()
        
print(DW_AUTH_TOKEN)
        
asset_headers = {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {DW_AUTH_TOKEN}",
}

## Define headers for chart update API.
headers = {
    "Accept": "*/*",
    "Content-Type": "text/csv",
}
map_path = "./data/cities/bc-cma-kelowna.geojson"

map = open(map_path)
map = json.load(map)

response = requests.request("PUT", f"https://api.datawrapper.de/v3/charts/{CHART_ID}/assets/{map_path}", headers=asset_headers, data=json.dumps(map))

print(response.text)

## Update chart.
# response = requests.request("GET", f"https://api.datawrapper.de/v3/charts/{CHART_ID}", headers=headers)
# print(response)