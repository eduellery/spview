# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 11:43:32 2014

@author: felipe
"""

import csv
import psycopg2

# ssh tunneled: ssh eltermann@143.106.60.97 -L 54321:localhost:5432
conn = psycopg2.connect("dbname='spview' user='postgres' host='localhost' port='54321' password='Zem5aEpEH6dB5aF'");
cur = conn.cursor()

##########
# LENTIDAO
"""
CREATE TABLE IF NOT EXISTS lentidao (
    id bigint primary key,
    dataHora text,
    idCorredor bigint,
    corredor text,
    sentido text,
    pista text,
    extensaoPista bigint,
    inicioLentidao text,
    terminoLentidao text,
    refNumericaInicioLentidao bigint,
    extensaoLentidao bigint,
    regiao text
);
CREATE INDEX corredor_idx ON lentidao (corredor);
CREATE INDEX regiao_idx ON lentidao (regiao);
COPY lentidao FROM '/home/eltermann/dados/lentidao/Lentidao-utf.csv.utf' DELIMITER ';' CSV;
"""

#############
# OCORRENCIAS
"""
CREATE TABLE IF NOT EXISTS ocorrencia (
    ocorrencia text,
    codigo bigint,
    local text,
    altura bigint,
    sentido text,
    pista text,
    faixaOcupacao text,
    totalFaixas text,
    inicio text,
    inicio_manual text,
    fim text,
    fim_manual text
)
CREATE INDEX codigo_idx ON ocorrencia (codigo);
COPY ocorrencia FROM '/home/eltermann/dados/ocorrencias/Ocorrencias.csv.utf' DELIMITER ';' CSV HEADER;
"""

################
# FALHA_SEMAFORO
"""
CREATE TABLE IF NOT EXISTS falha_semaforo (
    id_talao bigint primary key,
    local_lat text,
    local_long text,
    falha text,
    complemento text,
    prioridade bigint,
    causa text,
    informante text,
    numero	bigint,
    dataAbertura text,
    origemInformacao text,
    dataInformacao text,
    dataAcionamento text,
    dataChegada text,
    dataConfirmacao text,
    dataAcionamentoEletro text,
    dataCancelamentoEletro text,
    dataOrigem text,
    dataEncerramento text,
    observacoes text,
    status	bigint,
    motivoCancelamento text
)
"""
falha = {}
filename = '/home/felipe/hackathon-cet-2014-mar/dados-completos/semaforos/Falha.csv.utf'
with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=';')
  for row in csvreader:
    if row[0].isdigit():
      falha[row[0]] = row[1]
local = {}

filename = '/home/felipe/hackathon-cet-2014-mar/dados-completos/semaforos/Local.csv.utf'
with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=';')
  for row in csvreader:
    if row[0].isdigit():
      local[row[0]] = {'lat': row[4], 'lon': row[5]}

filename = '/home/felipe/hackathon-cet-2014-mar/dados-completos/semaforos/Talao_Falha.csv.utf'
with open(filename, 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=';')
  count = 0
  for row in csvreader:
    count += 1
    print(count)
    if row[0].isdigit() and row[1] in local and row[2] in falha:
      cur.execute("""INSERT INTO falha_semaforo VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
         (row[0], local[row[1]]['lat'], local[row[1]]['lon'], falha[row[2]], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]))

