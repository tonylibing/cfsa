from collections import defaultdict
import os
import io
import re
import codecs
import fileinput
import json
import timeit

import math
from textblob import TextBlob as tb
'''
encoding='utf-8'

def tf(word, blob):
    return blob.count(word) / len(blob)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    x = math.log(len(bloblist) / (1 + n_containing(word, bloblist)))
    return x

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

tic = timeit.default_timer()
f = open('segResult.txt','r')
for doc in f:
   bloblist = json.loads(doc)
f.close()
toc = timeit.default_timer()
print('Time elapsed: ',toc-tic,'s\n')

w = open('SWall.txt','w')
tic = timeit.default_timer()
for i, blob in enumerate(bloblist):
    scores = {word: tfidf(word, blob, bloblist) for word in blob}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print json.dumps(sorted_words)
    w.write(json.dumps(sorted_words)+'\n')
    toc = timeit.default_timer()
    print('Time elapsed: ',toc-tic,'s\n')
    tic = timeit.default_timer()
w.close()
'''

tic = timeit.default_timer()
f = open('segResult.txt','r')
for doc in f:
   d = json.loads(doc) 
f.close()
toc = timeit.default_timer()
print('Time elapsed: ',toc-tic,'s\n')

'''
for i in range(0,len(d)):
   for j in range(0,len(d[i])):
      print d[i][j]
'''
words = []
count = []
for i in range(0,len(d)):
   for j in range(0,len(d[i])):
      if d[i][j] not in words:
         words.append(d[i][j])
         count.append(1)
      else:
         count[words.index(d[i][j])] += 1
   print (i,j)
w = open('wordcount.txt','w')
for i in range(0,len(words)):
    w.write(words[i].encode('utf')+'\t'+str(count[i]))
w.close()
