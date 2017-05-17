import json
f = open('wordcount2.txt','r')
for doc in f:
   d = json.loads(doc)
f.close()

words = sorted(d, key=lambda x:x[1], reverse=True)

w = open('wordcountsorted.txt','w')
w.write(json.dumps(words))
w.close()
