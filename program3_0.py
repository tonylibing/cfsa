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
encoding='utf'

'''
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
f = open('project1/segResult.txt','r')
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
import bindings.frontend as ph
ph.env.pyhusky_start()

d_extend = []

for i in range(0,len(d)):
   for j in range(0,len(d[i])):
     d_extend.extend(d[i][j])
     print len(d_extend)

words = ph.env.parallelize(d_extend)

wordcount = words.map(lambda x:(x,1)).count_by_key().collect()

w = open('wordcount_0.txt','w')
w.write(json.dumps(wordcount))
w.close()
