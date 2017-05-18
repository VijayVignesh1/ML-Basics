import numpy as np
import os
os.chdir('E:\CourseraML\machine-learning-ex6\ex6')
file=open('SpamReady1.txt','r')
load=file.read()
load=load.split()
file=open('vocab.txt','r')
load1=file.read()
load1=load1.split()
mainload=[]
for i in xrange(1,len(load1),2):
        mainload.append(load1[i])
        
x=np.zeros((len(mainload),1))
for i in xrange(len(mainload)):
    for j in xrange(len(load)):
        if mainload[i]==load[j]:
            x[i]=1
print x

