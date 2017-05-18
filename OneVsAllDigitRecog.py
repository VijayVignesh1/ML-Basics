import numpy as np
import scipy.optimize as op
import pylab
from pylab import scatter,plot,show
import os
from scipy.io import loadmat
os.chdir('E:\CourseraML\machine-learning-ex3\ex3')
load=loadmat('ex3data1.mat')
x=load['X']
y=load['y']
def sigmoid(z):
    return 1/(1+np.exp(-z))
def CostFunc(theta,x,y,c,lam):
	m,n=x.shape
	theta=theta.reshape((n,1))
	y=y.reshape((m,1))
	y=(y==c)+0
	y=y.reshape(np.size(y),1)
	k=np.log(sigmoid(np.dot(x,theta)))
	l=np.log(1-sigmoid(np.dot(x,theta)))
	fin=y*k+(1-y)*l
	final=-np.sum(fin)/np.size(y)
	extra=lam/2.0*1.0/np.size(y)*(sum(theta**2)-theta[0]**2)
	return final+extra
def Gradient(theta,x,y,c,lam):
	m,n=x.shape
	theta=theta.reshape((n,1))
	y=y.reshape((m,1))
	y=(y==c)+0
	k=sigmoid(np.dot(x,theta))
	fi=np.dot(np.transpose(x),k-y)
	final=fi/np.size(y)
	extra=theta*(lam/np.size(y))
	grad=final+extra
	grad[0,0]=grad[0,0]-(theta[0,0]*(lam/np.size(y)))
	return grad
#x=np.append(np.ones((x.shape[0],1)),x,axis=1)
theta=np.zeros((x.shape[1],1))
print CostFunc(theta,x,y,1,0.01)
print Gradient(theta,x,y,1,0.01)
temp=1
opt_theta=np.zeros((1,x.shape[1]))
for i in xrange(0,5000,500):
    initial_theta=np.zeros((x.shape[1],1))
    res=op.minimize(CostFunc,x0=initial_theta,args=(x,y,temp,0.01,),method='SLSQP',jac=Gradient)
    temp+=1
    opt_theta=np.append(opt_theta,np.array([res.x]),axis=0)
opt_theta=opt_theta[1:,:]
