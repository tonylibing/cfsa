import json

f = open('numberedResult.txt','r')
for doc in f:
   d = json.loads(doc)
f.close()

w = open('numResultZH.txt','w')
for x in d:
  w.write(str(x[0])+' '+x[1].encode('utf')+'\n')
w.close()
