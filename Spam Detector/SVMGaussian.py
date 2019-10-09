import numpy as np
import os
import pylab
from pylab import plot,show,contour
import scipy.io
import sklearn
from sklearn import svm
from numpy import where
#os.chdir('E:\CourseraML\machine-learning-ex6\ex6')
load=scipy.io.loadmat('ex6data3.mat')
x=load['X']
y=load['y']
sigma=0.1
gamma=np.power(sigma,-2)
clf=svm.SVC(C=1,kernel='rbf',gamma=gamma)
clf.fit(x,y)
pos=where(y==1)
neg=where(y==0)
plot(x[pos,0],x[pos,1],'rx')
plot(x[neg,0],x[neg,1],'bo')
xvals=np.linspace(-1,1,100)
yvals=np.linspace(-1,1,100)
zvals=np.zeros((len(xvals),len(yvals)))
for i in range(len(xvals)):
    for j in range(len(yvals)):
        zvals[i][j]=float(clf.predict(np.array([xvals[i],yvals[j]]).reshape(1,-1)))
zvals=zvals.T
contour(xvals,yvals,zvals)
show()
xval=load['Xval']
yval=load['yval']
cs=[0.01,0.03,0.1,0.3,1,3,10,30]
sigs=[0.01,0.03,0.1,0.3,1,3,10,30]
k=np.zeros((len(cs),len(sigs)))
for i in range(len(cs)):
    for j in range(len(sigs)):
        gamma=sigs[j]**-2
        clf1=svm.SVC(C=cs[i],kernel='rbf',gamma=gamma)
        clf1.fit(x,y)
        k[i][j]=(float(np.sum(yval==clf1.predict(xval).reshape(200,1)))/np.size(yval))*100
#contour(np.array([cs]).reshape(8,),np.array([sigs]).reshape(8,),k)
#show()
a=[]
for i in range(8):
    a.append(k[i][k.argmax(axis=1)[i]])
a=np.array(a)
max_result=a[a.argmax()]
opt_C_val=k.argmax()%8+1
opt_sigma_val=k.argmax()-(opt_C_val*8)
print(cs[opt_C_val])
print(sigs[opt_sigma_val])
