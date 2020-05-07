import pandas as pd
import requests
import json
BASEURL = 'https://api.opencagedata.com/geocode/v1/json?key=23f5ddc46c3c459499de1d2056267c51&q='

def get_lat_lon(reg):
  raw = requests.get(BASEURL+reg)
  data = json.loads(raw.text)
  pos = data['results']
  response = None
  for res in pos:
    if (res['components']['ISO_3166-1_alpha-3'] == 'BRA'):
      # print(res['formatted'])
      response = res['geometry']
      break
  return response

xl = pd.ExcelFile("data/entregas.xlsx")
df = xl.parse("Sheet1").groupby(['CIDADE']).sum()

data = {}

for row in df.iterrows():
  loc = row[0]
  entregues = int(row[1])

  coor = get_lat_lon(loc)
  
  if coor is None:
    data[loc] = {
      'entregues': entregues,
    }
    continue
  
  lat = coor['lat']
  long = coor['lng']

  data[loc] = {
    'latitude': lat,
    'longitude': long,
    'entregues': entregues,
  }

  print(lat, long, entregues)


with open('data/data.json', 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=4)