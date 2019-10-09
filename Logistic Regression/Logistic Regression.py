import numpy as np
import scipy.optimize as op
import pylab
from pylab import scatter,plot,show
from numpy import where
import os
from numpy import loadtxt
#os.chdir('E:\CourseraML\machine-learning-ex2\ex2')
load=loadtxt('ex2data1.txt',delimiter=',')
x=load[:,0:2]
y=load[:,2]
x=np.append(np.ones((x.shape[0],1)),x,axis=1)
def sigmoid(z):
    return 1/(1+np.exp(-z))
def CostFunc(theta,x,y):
    m,n=x.shape
    theta=theta.reshape((n,1))
    y=y.reshape((m,1))
    k=np.log(sigmoid(np.dot(x,theta)))
    l=np.log(1-sigmoid(np.dot(x,theta)))
    fin=(y*k)+(1-y)*l
    final=-1.0/np.size(y)*np.sum(fin)
    return final
def Gradient(theta,x,y):
    m,n=x.shape
    theta=theta.reshape((n,1))
    y=y.reshape((m,1))
    k=sigmoid(np.dot(x,theta))
    fin=np.dot(np.transpose(x),k-y)*1.0/np.size(y)
    return fin
initial_theta=np.zeros((3,1))
print(CostFunc(initial_theta,x,y))
res=op.minimize(CostFunc,x0=initial_theta,args=(x,y,),method='SLSQP',jac=Gradient)
print(CostFunc(res.x,x,y))
print(res.fun)
xf=np.array([1,45,85])
print(sigmoid(np.dot(xf,res.x)))
pos=where(y==1)
neg=where(y==0)
scatter(x[pos,1],x[pos,2],marker='o',c='b')
scatter(x[neg,1],x[neg,2],marker='x',c='r')
a=np.linspace(0,100,1000)
b=np.linspace(0,100,1000)
z=np.zeros((np.size(a),np.size(b)))
for i in range(len(a)):
    for j in range(len(b)):
        z[i,j]=sigmoid(np.dot(np.array([1,a[i],b[j]]),res.x))
z=z.T
print(a.shape)
pylab.contour(a,b,z,linewidths=2,levels=[0.5])
plot(xf[1],xf[2],'x')
show()
