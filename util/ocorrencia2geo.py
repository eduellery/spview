# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 18:37:04 2014

@author: felipe
"""

from pygeocoder import Geocoder
from pygeolib import GeocoderError
import psycopg2

"""
ALTER TABLE ocorrencia ADD lat text;
ALTER TABLE ocorrencia ADD lon text;
"""

# ssh tunneled: ssh eltermann@143.106.60.97 -L 54321:localhost:5432
conn = psycopg2.connect("dbname='spview' user='postgres' host='localhost' port='5432' password='Zem5aEpEH6dB5aF'");
cur = conn.cursor()

geocoder = Geocoder()

cur.execute("""SELECT ocorrencia, local, altura FROM ocorrencia""")
result = cur.fetchall()
count = 0
for row in result:
  count += 1
  cod_ocorrencia = row[0]
  rua = row[1]
  altura = row[2]
  print(count)
  if altura and altura != 'NULL':
    address = '%s, %s' % (rua, altura)
  else:
    address = rua

  try:
    ret = geocoder.geocode(address)
    lat, lon = ret.coordinates
  except GeocoderError as e:
    lat, lon = ('', '')

  cur.execute("""UPDATE ocorrencia SET lat=%s, lon=%s WHERE ocorrencia=%s""", (lat, lon, cod_ocorrencia))
conn.commit()