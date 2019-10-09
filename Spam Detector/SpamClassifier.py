import numpy as np
import os
import sklearn
from sklearn import svm
import scipy.io
import pylab
from pylab import plot,show,contour
#os.chdir('E:\CourseraML\machine-learning-ex6\ex6')
load=scipy.io.loadmat('spamTrain.mat')
X=load['X']
y=load['y']
file=open('emailReady1.txt','r')
load=file.read()
print(load)
load=load.split()
print(load)
file=open('vocab.txt','r')
load1=file.read()
load1=load1.split()
mainload=[]
for i in range(1,len(load1),2):
        mainload.append(load1[i])
        
x=np.zeros((len(mainload),1))
for i in range(len(mainload)):
    for j in range(len(load)):
        if mainload[i]==load[j]:
            x[i]=1
print(np.where(x==1))
clf=svm.SVC(C=100,kernel='linear')
clf.fit(X,y)
print(X.shape)
print(clf.predict(x.reshape((1,-1))))
