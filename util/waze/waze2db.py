import pymongo
import requests
import time


def waze_fetch():
  """Download jams from Waze."""
  url = 'https://www.waze.com/row-rtserver/web/GeoRSS?os=60&atof=false&format=JSON&ma=200&mj=100&mu=100&sc=216672&jmu=0&types=alerts%2Cusers%2Ctraffic&left=-47.002189636230460&right=-46.25182342529297&bottom=-23.704664042303435&top=-23.40404600012711&_=1395559611984'
  headers = {
    'Host': 'www.waze.com',
    'Referer': 'https://www.waze.com/livemap',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
  }
  response = requests.get(url, headers=headers)

  if response.ok:
    data = response.json()
    if isinstance(data, dict) and 'jams' in data:
      return data['endTime'], data['jams']
  return (None, [])


if __name__ == '__main__':

  MONGO_HOST = 'localhost'
  MONGO_PORT = 27017
  MONGO_DB = 'waze'
  MONGO_COLLECTION = 'jams'

  conn = pymongo.Connection(MONGO_HOST, MONGO_PORT)
  collection = conn[MONGO_DB][MONGO_COLLECTION]
  collection.ensure_index('street')
  collection.ensure_index('endtime')


  while True:
    endtime, jams = waze_fetch()
    if endtime and jams:
      for jam in jams:
        if 'street' in jam:
          jam_id = '%s - %s' % (jam['street'], endtime)
          doc = {
            '_id': jam_id,
            'endtime': endtime,
            'street': jam['street'],
            'length': jam['length'],
            'line': jam['line'],
            'speed': jam['speed'],
          }
          collection.update({'_id': doc['_id']}, doc, True) #upsert
    
    time.sleep(60)