import csv
import pymongo


MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'waze'
MONGO_COLLECTION = 'jams'

conn = pymongo.Connection(MONGO_HOST, MONGO_PORT)
collection = conn[MONGO_DB][MONGO_COLLECTION]

filename = '/tmp/waze0840.csv'
with open(filename, 'w') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter=',')
  csvwriter.writerow(('lat', 'lon', 'hora', 'extensao', 'timestr'))

  for i in range(44):
    j = i+3
    brazil_timestr = '01/01/2013T%02d:%02d' % (i//2, 30*(i%2))
    mongo_timestr_from = '2014-03-23 %02d' % (j//2)
    mongo_timestr_to = '2014-03-23 %02d' % ((j+1)//2)
    print({'endtime': {'$gt': mongo_timestr_from, '$lt': mongo_timestr_to}})
    for doc in collection.find({'endtime': {'$gt': mongo_timestr_from, '$lt': mongo_timestr_to}}):
      mean_location = doc['line'][len(doc['line'])//2]
      #-23.771521 <= lat < -23.324602 AND -46.940675 <= lon < -46.394105
      if mean_location['y'] >= -23.771521 and mean_location['y'] < -23.324602 and \
         mean_location['x'] >= -46.940675 and mean_location['x'] < -46.394105:
        csvwriter.writerow((
          mean_location['y'],
          mean_location['x'],
          i,
          doc['length'],
          brazil_timestr
        ))

  csvfile.close()
print(filename)