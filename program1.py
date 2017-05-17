import json
import timeit

import os
import io
import re
import codecs
import fileinput

encoding='utf8'

path = ["part-0","part-1","part-2","part-3","part-4","part-5","part-6","part-7","part-8","part-9","part-10","part-11","part-12","part-13","part-14","part-15","part-16","part-17","part-18","part-19","part-20","part-21","part-22","part-23","part-24","part-25","part-26","part-27","part-28","part-29","part-30","part-31","part-32","part-33","part-34","part-35","part-36","part-37","part-38","part-39","part-40","part-41","part-42","part-43","part-44","part-45","part-46","part-47","part-48","part-49","part-50","part-51","part-52","part-53","part-54","part-55","part-56","part-57","part-58","part-59","part-60","part-61","part-62","part-63","part-64","part-65","part-66","part-67","part-68","part-69","part-70","part-71","part-72","part-73","part-74","part-75","part-76","part-77","part-78","part-79","part-80","part-81","part-82","part-83","part-84","part-85","part-86","part-87","part-88","part-89","part-90","part-91","part-92","part-93","part-94","part-95","part-96","part-97","part-98","part-99","part-100","part-101","part-102","part-103","part-104","part-105","part-106","part-107","part-108","part-109","part-110","part-111","part-112","part-113","part-114","part-115","part-116","part-117","part-118","part-119","part-120","part-121","part-122","part-123","part-124","part-125","part-126","part-127","part-128","part-129","part-130","part-131","part-132","part-133","part-134","part-135","part-136","part-137","part-138","part-139","part-140","part-141","part-142","part-143","part-144","part-145","part-146","part-147","part-148","part-149","part-150","part-151","part-152","part-153","part-154","part-155","part-156","part-157","part-158","part-159","part-160","part-161","part-162","part-163","part-164","part-165","part-166","part-167","part-168","part-169","part-170","part-171","part-172","part-173","part-174","part-175","part-176","part-177","part-178","part-179"]

print('Loading the data into the system for processing...')
tic = timeit.default_timer()
for i in range(0,len(path)):
    entries = []
    docs = []
    f = open(path[i],"r")
    for line in f:
        entry = json.loads(line)
        entries.append(entry)
        if entry['type']=='eastmoney_posts':
            docs.append(entry['posts_text'])
            for j in entry['comments']:
                docs.append(j['comment_text'])
        else:
            for j in entry['comments']:
                docs.append(j['comment_text'])
        toc = timeit.default_timer()
        print('Time elapsed: ',toc-tic,'s')
    f.close()
    toc = timeit.default_timer()
    print('File ', i, ' reading time: ',toc-tic,'s')
    w = open('docs'+str(i)+'.txt','w')
    w.write(json.dumps(docs))
    w.close()
