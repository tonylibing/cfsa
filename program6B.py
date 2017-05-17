import json

f = open('numberedResult.txt','r')
for doc in f:
   d = json.loads(doc)
f.close()

w = open('numResultZH0.txt','w')
n=0
for x in d:
  n+=1
  if x[1]!="":
    w.write(str(n)+' '+x[1].encode('utf')+'\n')
w.close()
