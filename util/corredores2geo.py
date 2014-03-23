# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 14:38:55 2014

@author: felipe
"""
import csv
from pygeocoder import Geocoder
from pygeolib import GeocoderError, GeocoderResult
import psycopg2


# ssh tunneled: ssh eltermann@143.106.60.97 -L 54321:localhost:5432
conn = psycopg2.connect("dbname='spview' user='postgres' host='localhost' port='54321' password='Zem5aEpEH6dB5aF'");
cur = conn.cursor()

geocoder = Geocoder()

#Abrir os enderecos
"""
COPY (SELECT corredor, count(*) from lentidao GROUP BY corredor) To '/home/eltermann/dados/lentidao/corredores.csv' WITH CSV;
"""
filename = '/home/felipe/hackathon-cet-2014-mar/dados-completos/lentidao/corredores.csv'
corredores = {}
with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  for row in csvreader:
    corredor = row[0]
    print(corredor)
    address = 'Brazil, SP, São Paulo, %s' % (corredor)
    try:
      ret = geocoder.geocode(address)
      corredores[corredor] = {'lat': ret.latitude, 'lon': ret.longitude}
    except GeocoderError as e:
      corredores[corredor] = False


filename = '/home/felipe/hackathon-cet-2014-mar/dados-completos/lentidao/corredores_geo.csv'
with open(filename, 'w') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter=',')
  for k, v in corredores.iteritems():
    csvwriter.writerow((k, v['lat'], v['lon']))
  csvfile.close()

filename = '/home/felipe/hackathon-cet-2014-mar/dados-completos/lentidao/corredores_geo2.csv'
with open(filename, 'w') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter=',')
  for k, v in corredores.iteritems():
    csvwriter.writerow((k, '%s,%s' % (v['lat'], v['lon'])))
  csvfile.close()


"""
ALTER TABLE lentidao ADD lat text;
ALTER TABLE lentidao ADD lon text;
"""
for k, v in corredores.iteritems():
  corredor = k
  lat = v['lat']
  lon = v['lon']
  print(corredor)
  cur.execute("""UPDATE lentidao SET lat=%s, lon=%s WHERE corredor=%s""", (lat, lon, corredor))
conn.commit()

filename = '/home/felipe/hackathon-cet-2014-mar/dados/corredores_errados.csv'
with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  for row in csvreader:
    corredor = row[0]
    lat = row[1]
    lon = row[2]
    print(corredor, lat, lon)
    cur.execute("""UPDATE lentidao SET lat=%s, lon=%s WHERE corredor=%s""", (lat, lon, corredor))
  conn.commit()
