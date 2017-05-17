import sys
reload(sys)
sys.setdefaultencoding('utf8')

import jieba
import os
import json
import timeit

wordcollect = [];

rootdir = 'eastmoney/'+sys.argv[1];

for folder, subs, files in os.walk(rootdir):
    with open(os.path.join(rootdir, 'wordcollect.txt'), 'w') as dest:
        for filename in files:
            if filename=='.DS_Store' or filename=='wordcollect.txt':
                continue
            tic = timeit.default_timer()
            with open(os.path.join(folder, filename), 'r') as src:
                content = src.read()
                seg_list = jieba.cut(content)
                for s in seg_list:
                    if s not in wordcollect:
                        wordcollect.append(s)
                        dest.write(s+'\n')
                toc = timeit.default_timer()
                print sys.argv[1],' ',filename, ' ', toc-tic
