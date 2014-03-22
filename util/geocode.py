from pygeocoder import Geocoder
from random import choice

proxy_list = [x.strip() for x in ['http://186.238.51.149:8080',
'http://189.39.124.54:80',
'http://190.128.136.194:80',
'http://177.36.214.214:8080',
'http://192.227.139.227:8089',
'http://172.245.59.203:7808',
'http://172.245.59.203:8089',
'http://172.245.59.203:8089',
'http://177.107.97.245:8080',
'http://198.27.97.214:8089',
'http://192.227.139.227:7808',
'http://198.27.97.214:7808',
'http://198.56.208.37:3127',
'http://200.153.105.1:8080',
'http://136.0.16.217:7808',
'http://200.42.56.146:8080',
'http://66.35.68.146:7808',
'http://189.39.124.54:80',
'http://23.23.77.156:80',
'http://190.122.186.197:8080',
'http://189.111.249.96:3128',
'http://200.153.105.1:8080',
'http://60.249.192.115:8080',
'http://200.195.141.178:8080',
'http://85.185.45.3:80',
'http://186.238.51.149:8080',
'http://201.44.177.132:3128',
'http://187.111.255.130:3128',
'http://111.1.55.19:8080',
'http://187.125.147.178:3128',
'http://189.108.118.194:8080',
'http://200.110.243.150:3128',
'http://187.111.192.3:8080',
'http://123.183.220.217:80',
'http://177.159.166.202:3128',
'http://85.185.45.237:80',
'http://94.228.205.2:8080',
'http://66.35.68.146:7808',
'http://192.227.247.178:7808',
'http://187.72.175.250:2020',
'http://2.183.155.2:8082',
'http://190.122.185.212:8080',
'http://203.204.206.176:3128',
'http://64.156.80.36:80',
'http://184.164.75.33:7808',
'http://177.103.139.64:3128',
'http://221.226.110.198:80',
'http://85.185.45.194:80',
'http://201.218.59.122:3128',
'http://202.116.1.149:8128',
'http://202.116.1.148:8128',
'http://201.218.59.122:3128',
'http://114.141.162.53:8080',
'http://66.35.68.146:8089',
'http://200.196.51.130:8080',
'http://177.124.60.91:3128',
'http://174.34.166.10:3128',
'http://1.179.147.2:8080',
'http://217.12.113.67:443',
'http://172.245.59.203:7808',
'http://200.192.150.2:8080',
'http://203.146.82.253:3128',
'http://66.143.243.214:8080',
'http://119.97.146.16:80',
'http://186.167.32.115:8080',
'http://221.210.5.50:8080',
'http://192.227.139.227:8089',
'http://203.172.208.43:3129',
'http://123.183.220.126:80',
'http://190.200.217.16:8080',
'http://202.118.236.130:3128',
'http://178.48.2.237:80',
'http://66.35.68.145:8089',
'http://181.112.217.211:8080',
'http://208.110.67.122:7808',
'http://85.114.141.191:80',
'http://189.9.0.153:80',
'http://202.101.96.154:8888',
'http://217.169.209.2:6666',
'http://172.245.59.203:3127',
'http://200.158.220.185:3128',
'http://41.221.216.18:8080',
'http://190.0.9.202:8080',
'http://190.151.10.226:8080',
'http://110.77.142.241:8080',
'http://218.25.17.246:80',
'http://218.92.227.165:23685',
'http://221.226.110.198:80',
'http://64.34.14.28:8089',
'http://85.90.60.133:80',
'http://181.112.217.211:8080']]



#Abrir os enderesos
with open('bla.txt') as f:
  cities  = f.readlines()

s = open('succes.txt' ,'w')
t = open('fail.txt','w')
count = 0
fail = []
dic_lat = {}
dic_city = {}


from pygeolib import GeocoderError, GeocoderResult
geocoder = Geocoder()
count=0
#Cada i é um endereço
for i in cities[count:]:
  #geocoder.set_proxy('http://186.233.35.26:3128')
  try:
    results = geocoder.geocode(i)
    if dic_lat.has_key(results.coordinates):
      dic_lat[results.coordinates].append(i)
    else:
      dic_lat[results.coordinates] = [i]
    dic_city[i] = results.coordinates
    count+=1
    print count
    print i, results.coordinates
    #time.sleep(1)
    s.write(str(i)+'\t' + str(results.coordinates) + '\n')
  except GeocoderError as e:
    if e.status == 'ZERO_RESULTS':
      count +=1
      continue
    print "Error({0}): blah".format(e.status)
    break
  except:
    count +=1
    t.write(i+'\n')

