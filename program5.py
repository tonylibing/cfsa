from collections import defaultdict
import os
import io
import re
import codecs
import fileinput
import json
import timeit

encoding='utf-8'

tic = timeit.default_timer()
f = open('segResult.txt','r')
for doc in f:
   d = json.loads(doc)
f.close()
toc = timeit.default_timer()
print('Time elapsed: ',toc-tic,'s\n')

tic = timeit.default_timer()
words = [j for i in d for j in i]
toc = timeit.default_timer()
print('Time elapsed: ',toc-tic,'s\n')

w = open('wordcount1.txt','w')
w.write(json.dumps(words))
w.close()
