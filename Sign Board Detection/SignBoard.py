import numpy as np
import pandas as pd
import os
from sklearn import svm
from sklearn.linear_model import LogisticRegression
#os.chdir('E:\\Kaggle Datasets\\Sign Board Detection')
load=pd.read_csv("train.csv")
x=load.values[:,2:4]
#print(x)
k=np.zeros((np.size(x[:,0]),1))
for i in range(np.size(k)):
	if load.values[i,1]=='Front':
		k[i]=1
	if load.values[i,1]=='Left':
		k[i]=2
	if load.values[i,1]=='Rear':
		k[i]=3
	if load.values[i,1]=='Right':
		k[i]=4
y=np.zeros((np.size(x[:,0]),1))
for i in range(np.size(y)):
	if load.values[i,6]=='Front':
		y[i]=1
	if load.values[i,6]=='Left':
		y[i]=2
	if load.values[i,6]=='Rear':
		y[i]=3
	if load.values[i,6]=='Right':
		y[i]=4
#print("hf")
x=np.append(k,x,axis=1)
#x_train=x[:25000,:]
#y_train=y[:25000,:]
#x_val=x[25000:,:]
#y_val=y[25000:,:]
#clf.fit(x_train,y_train)
#temp=0
#for i in xrange(np.size(y_val)):
#	if clf.predict(x_val[i])==y_val[i]:
#		temp+=1
#print temp/float(np.size(y_val))
load_test=pd.read_csv("test.csv")
tempp=np.zeros((load_test.values.shape[0],1))
for i in range(np.size(tempp)):
	if load_test.values[i,1]=='Front':
		tempp[i]=1
	if load_test.values[i,1]=='Left':
		tempp[i]=2
	if load_test.values[i,1]=='Rear':
		tempp[i]=3
	if load_test.values[i,1]=='Right':
		tempp[i]=4
final=np.zeros((load_test.values.shape[0],1))
final=load_test.values[:,0]
logistic=LogisticRegression()
logistic.fit(x,y)
x_test=np.append(tempp,load_test.values[:,2:4],axis=1)
final=np.append(final.reshape(31485,1),logistic.predict_proba(x_test),axis=1)
fin=pd.DataFrame(final)
#print("afd")
fin.to_csv('Predict.csv')
#print(fin)
