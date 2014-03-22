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

def processa_ocorrencias(params):
  cod_from = params['cod_from']
  cod_to = params['cod_to']
  proxy = params['proxy']
  
  geocoder = Geocoder()
  geocoder.set_proxy(proxy)

  # ssh tunneled: ssh eltermann@143.106.60.97 -L 54321:localhost:5432
  conn = psycopg2.connect("dbname='spview' user='postgres' host='localhost' port='5432' password='Zem5aEpEH6dB5aF'");
  cur = conn.cursor()

  cur.execute("""SELECT ocorrencia, local, altura FROM ocorrencia WHERE ocorrencia >= %s AND ocorrencia <= %s""", (cod_from, cod_to))
  result = cur.fetchall()
  count = 0
  for row in result:
    count += 1
    cod_ocorrencia = row[0]
    rua = row[1]
    altura = row[2]
    print(count)
    if altura and altura != 'NULL':
      address = 'Brazil, SP, São Paulo, %s, %s' % (rua, altura)
    else:
      address = 'Brazil, SP, São Paulo, %' % (rua)
  
    try:
      ret = geocoder.geocode(address)
      lat, lon = ret.coordinates
    except GeocoderError as e:
      lat, lon = ('', '')
  
    cur.execute("""UPDATE ocorrencia SET lat=%s, lon=%s WHERE ocorrencia=%s""", (lat, lon, cod_ocorrencia))
    if count % 100 == 0:
      conn.commit() # commita a cada 100

  conn.commit()
  return

n_threads = 8
p = Pool(n_threads)

cod_min = 10495901
cod_max = 22210785

params = []
cod_range = range(cod_min, cod_max, (cod_max-cod_min)//n_threads)
for i in range(n_threads):
  params.append({
    'proxy': random.choice(proxy_list),
    'cod_from': 'C%s' % (cod_range[i]),
    'cod_to': 'C%s' % (cod_range[i+1]),
  })

p.map(processa_ocorrencias, params)
