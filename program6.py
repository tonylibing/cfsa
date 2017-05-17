import json

f = open('wordcountsorted.txt','r')
for doc in f:
   d = json.loads(doc)
f.close()

w = open('tojinning0.txt','w')
for x in d:
  w.write(x[0].encode('utf')+' '+str(x[1])+'\n')
w.close()
