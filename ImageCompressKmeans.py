import numpy as np
import scipy.io
import cv2
import os
from numpy import where
from PIL import Image
os.chdir('E:\CourseraML\machine-learning-ex7\ex7')
load=cv2.imread('cat.9.jpg')
x=load
x=x.reshape(load.shape[0]*load.shape[1],load.shape[2])
x=x.astype(np.float)
x=x/255
centroid=np.random.rand(16,3)
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
    #c=c.reshape(np.size(c),1)
    for i in xrange(16):
        k=where(c==i)
        centroid[i]=np.array([np.mean(x[k,:],axis=1)])
        '''for j in xrange(3):
            if np.size(k)==0:
                centroid[i]=np.random.rand(1,3)
                #centroid[i]=np.zeros((1,3))
                break
            centroid[i][j]=np.sum(x[k,j])/float(np.size(k))'''
x_altered=centroid[c,:]
x_altered*=255
x_altered=x_altered.astype(np.uint8)
x_altered=x_altered.reshape(load.shape[0],load.shape[1],load.shape[2])
img=Image.fromarray(x_altered,'RGB')
img.save('E:\\CompressedImg.png')
