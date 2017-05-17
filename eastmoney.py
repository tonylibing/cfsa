import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

positive = open('positive.txt','r')
negative = open('negative.txt','r')

pos = []
neg = []

for p in positive:
    pos.append(p)
for n in negative:
    neg.append(n)

positive.close()
negative.close()

import ntpath
ntpath.basename("a/b/c")
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

import jieba
import os
import json
import timeit

rootdir = 'eastmoney' #sys.argv[1]
num_worker = 20
worker_id = int(sys.argv[-1])

for folder, subs, files in os.walk(rootdir):
    with open(os.path.join(folder, 'python-outfile.txt'), 'w') as dest:
        for filename in files:
            if hash(filename)%num_worker != worker_id: continue
            if filename=='.DS_Store' or filename=='python-outfile.txt':
                continue
            tic = timeit.default_timer()
            with open(os.path.join(folder, filename), 'r') as src:
                pcount=0
                ncount=0
                content = src.read()
                seg_list = jieba.cut(content)
                for s in seg_list:
                    if s in pos:
                        pcount+=1
                    elif s in neg:
                        ncount+=1
                name = filename.split('.')[0]+'\t'+str(pcount)+','+str(ncount)+'\n'
                dest.write(name)
                toc = timeit.default_timer()
                print toc-tic
                
                
                 

