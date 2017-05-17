import sys
reload(sys)
sys.setdefaultencoding('utf8')

import jieba
import os
import json
import timeit

wordcollect = [];

rootdir = 'eastmoney/'+sys.argv[1]
wordcollectfile = rootdir+'/wordcollect.txt'

f = open(wordcollectfile, 'r')

for l in f:
    l = l[0:-1]
    wordcollect.append(l)

f.close()

w = open(rootdir+'/basevector.txt', 'w')

w.write(json.dumps(wordcollect))

w.close()
