import numpy as np
import os
import scipy.optimize
from numpy import loadtxt
from pylab import show,scatter,plot
import pylab
#os.chdir('E:\CourseraML\machine-learning-ex1\ex1');
load=loadtxt('ex1data1.txt',delimiter=',')
x=load[:,0]
x=x.reshape(x.shape[0],1)
x=np.append(np.ones((np.size(x),1)),x,axis=1)
y=load[:,1]
y=y.reshape(y.shape[0],1)
theta=np.zeros((x.shape[1],1))
def CostFunc(theta,x,y):
    return (1.0/2.0*1.0/np.size(y)*sum((np.dot(x,theta)-y)**2))
print(CostFunc(theta,x,y))
for i in range(3000):
    del_1=1.0/np.size(y)*sum((np.dot(x,theta)-y)*x[:,0].reshape((97,1)))
    del_2=1.0/np.size(y)*sum((np.dot(x,theta)-y)*x[:,1].reshape((97,1)))
    theta=theta-0.01*np.array([del_1,del_2])
print(CostFunc(theta,x,y))
print(theta)
#print np.dot(np.array([1,5]),theta)
plot(x[:,1],y,'x',c='r')
plot(x[:,1],np.dot(x,theta))
show()
a=np.linspace(-10,10,100)
b=np.linspace(-1,4,100)
z=np.zeros((np.size(a),np.size(b)))
for i in range(len(a)):
    for j in range(len(b)):
        t=np.array([a[i],b[j]]).reshape(2,1)
        z[i,j]=CostFunc(t,x,y)
z=z.T
pylab.contour(a,b,z,np.logspace(-2,3,20))
plot(theta[0],theta[1],'x',c='r')
show()

