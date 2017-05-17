import sys

f = open(sys.argv[1],'r')

w2v = []

for l in f:
   print l[0:10]
   w2v.append(l)

f.close()

w2v.sort()

w = open('sorted'+sys.argv[1],'w')

for i in range(0,len(w2v)):
   w.write(w2v[i])

w.close()
