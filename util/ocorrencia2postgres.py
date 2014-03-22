# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 18:19:05 2014

@author: felipe
"""

import csv
import psycopg2

# ssh tunneled: ssh eltermann@143.106.60.97 -L 54321:localhost:5432
conn = psycopg2.connect("dbname='spview' user='postgres' host='localhost' port='5432' password='Zem5aEpEH6dB5aF'");
cur = conn.cursor()

#############
# OCORRENCIAS
"""
CREATE TABLE IF NOT EXISTS ocorrencia (
    ocorrencia text,
    tipo text,
    local text,
    altura text,
    sentido text,
    pista text,
    faixaOcupacao text,
    totalFaixas text,
    inicio text,
    inicio_manual text,
    fim text,
    fim_manual text
)
COPY ocorrencia FROM '/home/eltermann/dados/ocorrencias/Ocorrencias.csv.utf' DELIMITER ';' CSV HEADER;
"""
codigo_ocorrencia = {
  '205': 'auto moto ou utilitário imobilizado na via',
  '207': 'caminhão imobilizado na via',
  '302': 'acidente de trânsito com vítima',
  '303': 'acidente de trânsito sem vítima',
}

filename = '/home/eltermann/dados/Ocorrencias.zip.d/Ocorrencias.csv.utf'
with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=';')
  count = 0
  for row in csvreader:
    count += 1
    print(count)
    if count > 1 and row[1] in codigo_ocorrencia:
      cur.execute("""INSERT INTO ocorrencia VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
         (row[0], codigo_ocorrencia[row[1]], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
conn.commit()
