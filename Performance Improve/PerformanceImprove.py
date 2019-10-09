import numpy as np
import os
import pylab
from pylab import show,scatter,plot
import scipy.io
import scipy.optimize as op
import matplotlib.pyplot as plt
#os.chdir('E:\CourseraML\machine-learning-ex5\ex5')
load=scipy.io.loadmat('ex5data1.mat')
def CostFunc(theta,x,y,lam):
    m,n=x.shape
    theta=theta.reshape((n,1))
    y=y.reshape((m,1))
    k=1.0/2.0*1.0/np.size(y)*np.sum((np.dot(x,theta)-y)**2)
    extra=lam/2.0*1.0/np.size(y)*np.sum(theta[1:])
    return k+extra
def Gradient(theta,x,y,lam):
    m,n=x.shape
    theta=theta.reshape((n,1))
    y=y.reshape((m,1))
    k=1.0/np.size(y)*np.dot(np.transpose(x),np.dot(x,theta)-y)
    extra=lam/np.size(y)*theta
    k[1:]=k[1:]+extra[1:]
    return k
def LearningCurve(x,y,xval,yval,lam):
    error_train=[]
    error_val=[]
    theta=np.zeros((x.shape[1],1))
    for i in range(1,np.size(y)+1):
        res1=op.minimize(CostFunc,x0=theta,args=(x[:i,:],y[:i],lam,),method='SLSQP',jac=Gradient)
        error_train.append(CostFunc(res1.x,x[:i,:],y[:i],0))
        error_val.append(CostFunc(res1.x,xval,yval,0))
    return error_train,error_val
def PolyFeatures(x,p):
    for i in range(2,p+1):
        x=np.append(x,(x[:,1]**i).reshape(x.shape[0],1),axis=1)
    return x
def FeatureNormalize(x):
    mean=np.mean(x,axis=0)
    std=np.std(x,axis=0)
    x[:,1:]=(x[:,1:]-mean[1:])/std[1:]
    return x,mean,std
def ValidationCurve(x,y,xval,yval):
    train_err=[]
    val_err=[]
    lmda=[]
    rangeaxis=[0,0.001,0.003,0.01,0.03,0.1,0.3,1,3,10]
    theta=np.zeros((x.shape[1],1))
    for i in rangeaxis:
        res3=op.minimize(CostFunc,x0=theta,args=(x,y,i,),method='SLSQP',jac=Gradient)
        train_err.append(CostFunc(res3.x,x,y,0))
        val_err.append(CostFunc(res3.x,xval,yval,0))
        lmda.append(i)
    return train_err,val_err,lmda    
x=load['X']
y=load['y']
xval=load['Xval']
yval=load['yval']
yval=yval.reshape(np.size(yval),1)
x=np.append(np.ones((x.shape[0],1)),x,axis=1)
xval=np.append(np.ones((xval.shape[0],1)),xval,axis=1)
theta=np.zeros((x.shape[1],1))
res=op.minimize(CostFunc,x0=theta,args=(x,y,0,),method='SLSQP',jac=Gradient)
scatter(x[:,1],y,marker='x',c='r')
plot(x[:,1],np.dot(x,res.x),'b-')
show()
train,val=LearningCurve(x,y,xval,yval,0.01)
m=[i for i in range(1,np.size(y)+1)]
plot(m,train,'r-')
plot(m,val,'b-')
show()
lam=3
Xpoly=PolyFeatures(x,8)
Xpoly,mu,sigma=FeatureNormalize(Xpoly)
theta=np.zeros((Xpoly.shape[1],1))
res2=op.minimize(CostFunc,x0=theta,args=(Xpoly,y,lam,),method='SLSQP',jac=Gradient)
theta=res2.x
n=50
xaxis=np.linspace(x[:,1][np.argmin(x[:,1])],x[:,1][np.argmax(x[:,1])],n)
yaxis=np.ones((n,1))
yaxis=np.append(yaxis,xaxis.reshape(xaxis.shape[0],1),axis=1)
yaxis=PolyFeatures(yaxis,8)
yaxis[:,1:]=yaxis[:,1:]-mu[1:]
yaxis[:,1:]=yaxis[:,1:]/sigma[1:]
plot(x[:,1],y,'rx')
plot(xaxis,np.dot(yaxis,theta),'b--')
show()
XpolyVal=PolyFeatures(xval,8)
XpolyVal,mu1,sigma1=FeatureNormalize(XpolyVal)
train1,val1=LearningCurve(Xpoly,y,XpolyVal,yval,lam)
plot(m,train1,'b-')
plot(m,val1,'r-')
show()
y_norm=(y-np.mean(y))/np.std(y)
yval_norm=(yval-np.mean(yval))/np.std(yval)
train2,val2,lmda=ValidationCurve(Xpoly,y_norm,XpolyVal,yval_norm)
plot(lmda,train2,'r-')
plot(lmda,val2,'b-')
show()
