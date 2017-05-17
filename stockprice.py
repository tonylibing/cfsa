import sys
import os
f = open(sys.argv[1],'r')
price = []
for l in f:
  line = l.split(',')
  if line[2] <= '2017-01-20':
    entry = []
    entry.extend(line[2:7])
    entry.extend(line[9:10])
    price.append(entry)
f.close()

w = open('stat_price_'+sys.argv[1],'w')
for i in range(0,len(price)):
  entry = ','.join(price[i])+'\n'
  w.write(entry)
w.close()
