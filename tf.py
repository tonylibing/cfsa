import timeit
import json

tic = timeit.default_timer()
f = open('segResult.txt','r')
for doc in f:
  cm = json.loads(doc)
f.close()

for i in range(0,len(cm)):
  cm[i] = cm[i][0]

tf = []
cmd = []

print len(cm)
for n in range(0,len(cm)):
    cc = []
    cd = []
    for t in cm[n]:
        if t not in cd:
            cd.append(t)
            cc.append(float(cm[n].count(t)) / len(cm[n]))
    cmd.append(cd)
    tf.append(cc)
    toc = timeit.default_timer()
    print(n, '\tTime elapsed: ',toc-tic,' sec')

print('--------------------------------------------------')
w = open('TF.txt','w')
termfreq = []
for i in range(0,len(cmd)):
    tic = timeit.default_timer()
    line = []
    for j in range(0,len(tf[i])):
        line.append([cmd[i][j],tf[i][j]])
    w.write(json.dumps(line))
    w.write('\n')
    toc = timeit.default_timer()
    print(i,' ',len(cmd), 'Time elapsed: ',toc-tic,' sec')
w.close()
