import json

f = open('sorted.txt','r')

content = []
for l in f:
  content.append(l) 

f.close()

sentiment = []
stock = []
for i in range(0,len(content)):
  if i % 3==0:
    stock.append(content[i][0:-1])
  if i % 3==2:
    sentiment.append(json.loads(content[i]))

stat_sen=[]
for i in range(0,len(sentiment)):
  stat_sen.append([])
  for j in range(0,len(sentiment[i])):
    if sentiment[i][j][0:10] >= '2016-01-04':
      stat_sen[i].append(sentiment[i][j]) 
'''
for i in range(0,len(sentiment)):
   f = open('stat_sen'+stock[i]+'.txt','w')
   f.write(json.dumps(stat_sen[i]))
   f.close();
'''

for i in range(0,len(sentiment)):
   f = open('stat_sen'+stock[i]+'.csv','w')
   for j in stat_sen[i]:
     line = j.split('\t')
     f.write(line[0])
     f.write(',') 
     f.write(line[1])
   f.close();
