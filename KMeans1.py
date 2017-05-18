import numpy as np
import scipy.io
import pylab
from pylab import plot,show
from numpy import where
import os
os.chdir('E:\CourseraML\machine-learning-ex7\ex7')
load=scipy.io.loadmat('ex7data2.mat')
x=load['X']
centroid=np.random.rand(3,2)
for k in xrange(8):
    c=[]
    for i in x:
        min1=1000
        min_index=0
        for j in xrange(len(centroid)):
            if np.sum((i-centroid[j])**2)<min1:
                min1=np.sum((i-centroid[j])**2)
                min_index=j
        c.append(min_index)
    c=np.array(c)
    for i in xrange(3):
        k=where(c==i)
        for j in xrange(2):
            centroid[i][j]=np.sum(x[k,j])/float(np.size(k))
    #print centroid
    l=where(c==0)
    m=where(c==1)
    n=where(c==2)
    plot(x[l,0],x[l,1],'rx')
    plot(x[m,0],x[m,1],'gx')
    plot(x[n,0],x[n,1],'bx')
    plot(centroid[:,0],centroid[:,1],'bo')
    show()
    

