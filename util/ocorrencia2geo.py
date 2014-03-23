# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 18:37:04 2014

@author: felipe
"""

from multiprocessing import Pool
from pygeocoder import Geocoder
from pygeolib import GeocoderError
import psycopg2
import random

from proxies import proxy_list

"""
ALTER TABLE ocorrencia ADD lat text;
ALTER TABLE ocorrencia ADD lon text;
"""

def processa_ocorrencias():
  geocoder = Geocoder()

  # ssh tunneled: ssh eltermann@143.106.60.97 -L 54321:localhost:5432
  conn = psycopg2.connect("dbname='spview' user='postgres' host='localhost' port='5432' password='Zem5aEpEH6dB5aF'");
  cur = conn.cursor()

  cur.execute("""SELECT logradouro, numero FROM endereco""")
  result = cur.fetchall()
  count = 0
  for row in result:
    print(row)
    count += 1
    rua = row[0]
    altura = row[1]

    address = 'Brazil, SP, São Paulo, %s %s' % (rua, altura)
    try:
      ret = geocoder.geocode(address)
      lat = ret.latitude
      lon = ret.longitude
    except GeocoderError as e:
      lat, lon = ('', '')
  
    cur.execute("""UPDATE endereco SET lat=%s, long=%s WHERE logradouro=%s AND numero=%s""", (lat, lon, rua, altura))
    conn.commit()
  return

processa_ocorrencias()
