import numpy as np
import os
import pylab
from pylab import plot,show,contour
import scipy.io
import sklearn
from sklearn import svm
from numpy import where
os.chdir('E:\CourseraML\machine-learning-ex6\ex6')
load=scipy.io.loadmat('ex6data1.mat')
x=load['X']
y=load['y']
clf=svm.SVC(C=100,kernel='linear')
clf.fit(x,y)
pos=where(y==1)
neg=where(y==0)
plot(x[pos,0],x[pos,1],'rx')
plot(x[neg,0],x[neg,1],'bo')
xvals=np.linspace(0,5,100)
yvals=np.linspace(0,5,100)
zvals=np.zeros((len(xvals),len(yvals)))
for i in xrange(len(xvals)):
    for j in xrange(len(yvals)):
        zvals[i][j]=float(clf.predict(np.array([xvals[i],yvals[j]])))
zvals=zvals.T
contour(xvals,yvals,zvals)
show()
