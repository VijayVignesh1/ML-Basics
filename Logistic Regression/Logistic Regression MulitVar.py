import numpy as np
import os
from numpy import loadtxt
import scipy.optimize as op
import pylab
from pylab import show,scatter,plot,contour
from numpy import where
#os.chdir('E:\CourseraML\machine-learning-ex2\ex2')
load=loadtxt('ex2data2.txt',delimiter=',')
x=load[:,:2]
y=load[:,2]
pos=where(y==1)
neg=where(y==0)
plot(x[pos,0],x[pos,1],'rx')
plot(x[neg,0],x[neg,1],'bx')
def FeatureMap(x1,x2,p):
    out=np.ones((x1.shape[0],1))
    out=np.insert(x1,0,1,axis=1)
    out=np.append(out,x2,axis=1)
    for i in range(2,p+1):
        for j in range(i+1):
            out=np.append(out,((x1**j)*(x2**(i-j))).reshape(x1.shape[0],1),axis=1)
    return out
def sigmoid(z):
    return 1/(1+np.exp(-z))
def CostFunc(theta,x,y,lam):
    m,n=x.shape
    theta=theta.reshape(n,1)
    y=y.reshape(m,1)
    k=np.log(sigmoid(np.dot(x,theta)))
    l=np.log(1-sigmoid(np.dot(x,theta)))
    fin=y*k+(1-y)*l
    final=-1.0/np.size(y)*sum(fin)
    extra=lam/2.0*1.0/np.size(y)*sum(theta[1:])
    return final+extra
def Gradient(theta,x,y,lam):
    m,n=x.shape
    theta=theta.reshape(n,1)
    y=y.reshape(m,1)
    k=1.0/np.size(y)*np.dot(np.transpose(x),sigmoid(np.dot(x,theta))-y)
    extra=lam/np.size(y)*theta
    grad=k+extra
    grad[0,0]=grad[0,0]-lam/np.size(y)*theta[0]
    return grad
def FeatureMap1(a,b,p):
    out=np.array([1,a,b])
    for i in range(2,p+1):
        for j in range(i+1):
            out=np.append(out,(a**j)*(b**(i-j)))
    return out
x=np.append(np.ones((x.shape[0],1)),x,axis=1)
x=FeatureMap(load[:,0].reshape(x.shape[0],1),load[:,1].reshape(x.shape[0],1),6)
theta=np.zeros((x.shape[1],1))
print(CostFunc(theta,x,y,0.01))
#print Gradient(theta,x,y,0.01)
res=op.minimize(CostFunc,x0=theta,args=(x,y,0.01,),method='SLSQP',jac=Gradient)
#print(res.x)
a=np.linspace(-1,1.5,50)
b=np.linspace(-1,1.5,50)
z=np.zeros((len(a),len(b)))
for i in range(len(a)):
    for j in range(len(b)):
        t=FeatureMap1(a[i],b[j],6)
        z[i,j]=(np.dot(t,res.x))
z=z.T
contour(a,b,z)
show()
