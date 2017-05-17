from collections import defaultdict
import os
import io
import re
import codecs
import fileinput
import json
import timeit

encoding='utf-8'

path = ["docs0.txt","docs1.txt","docs2.txt","docs3.txt","docs4.txt","docs5.txt","docs6.txt","docs7.txt","docs8.txt","docs9.txt","docs10.txt","docs11.txt","docs12.txt","docs13.txt","docs14.txt","docs15.txt","docs16.txt","docs17.txt","docs18.txt","docs19.txt","docs20.txt","docs21.txt","docs22.txt","docs23.txt","docs24.txt","docs25.txt","docs26.txt","docs27.txt","docs28.txt","docs29.txt","docs30.txt","docs31.txt","docs32.txt","docs33.txt","docs34.txt","docs35.txt","docs36.txt","docs37.txt","docs38.txt","docs39.txt","docs40.txt","docs41.txt","docs42.txt","docs43.txt","docs44.txt","docs45.txt","docs46.txt","docs47.txt","docs48.txt","docs49.txt","docs50.txt","docs51.txt","docs52.txt","docs53.txt","docs54.txt","docs55.txt","docs56.txt","docs57.txt","docs58.txt","docs59.txt","docs60.txt","docs61.txt","docs62.txt","docs63.txt","docs64.txt","docs65.txt","docs66.txt","docs67.txt","docs68.txt","docs69.txt","docs70.txt","docs71.txt","docs72.txt","docs73.txt","docs74.txt","docs75.txt","docs76.txt","docs77.txt","docs78.txt","docs79.txt","docs80.txt","docs81.txt","docs82.txt","docs83.txt","docs84.txt","docs85.txt","docs86.txt","docs87.txt","docs88.txt","docs89.txt","docs90.txt","docs91.txt","docs92.txt","docs93.txt","docs94.txt","docs95.txt","docs96.txt","docs97.txt","docs98.txt","docs99.txt","docs100.txt","docs101.txt","docs102.txt","docs103.txt","docs104.txt","docs105.txt","docs106.txt","docs107.txt","docs108.txt","docs109.txt","docs110.txt","docs111.txt","docs112.txt","docs113.txt","docs114.txt","docs115.txt","docs116.txt","docs117.txt","docs118.txt","docs119.txt","docs120.txt","docs121.txt","docs122.txt","docs123.txt","docs124.txt","docs125.txt","docs126.txt","docs127.txt","docs128.txt","docs129.txt","docs130.txt","docs131.txt","docs132.txt","docs133.txt","docs134.txt","docs135.txt","docs136.txt","docs137.txt","docs138.txt","docs139.txt","docs140.txt","docs141.txt","docs142.txt","docs143.txt","docs144.txt","docs145.txt","docs146.txt","docs147.txt","docs148.txt","docs149.txt","docs150.txt","docs151.txt","docs152.txt","docs153.txt","docs154.txt","docs155.txt","docs156.txt","docs157.txt","docs158.txt","docs159.txt","docs160.txt","docs161.txt","docs162.txt","docs163.txt","docs164.txt","docs165.txt","docs166.txt","docs167.txt","docs168.txt","docs169.txt","docs170.txt","docs171.txt","docs172.txt","docs173.txt","docs174.txt","docs175.txt","docs176.txt","docs177.txt","docs178.txt","docs179.txt"]

numberedResult = []

print('Numbering the sentences...')
tic = timeit.default_timer()
id=0
for i in range(0,len(path)):
    f = open(path[i],'r')
    for doc in f:
        d = json.loads(doc)
        for line in d:
            numberedResult.append([id,line]) 
            id+=1
    toc = timeit.default_timer()
    print('File '+str(i)+' processing time: '+str(toc-tic)+'s')

# backup numberedResult!
w = open('numberedResult.txt','w')
w.write(json.dumps(numberedResult))
w.close()
