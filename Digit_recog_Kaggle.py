import random
import numpy as np
import csv
def data_loader():
    import csv as csv
    csv_obj=csv.reader(open('E:\\train.csv','rb'))
    header=csv_obj.next()
    data=[]
    for row in csv_obj:
        data.append(row)
    data_main=[]
    for i in xrange(len(data)):
        temp=[0]*10
        temp[int(data[i][0])]=1
        y=np.array([[temp]],dtype=np.float32).reshape(10,1)
        #y=np.array([[data[i][0]]],dtype=np.float32)
        x=np.array([[data[i][1:]]],dtype=np.float32).reshape(784,1)
        x/=256
        temp=(x,y)
        data_main.append(temp)
    csv_obj1=csv.reader(open('E:\\test.csv','rb'))
    header1=csv_obj1.next()
    data1=[]
    for row in csv_obj1:
        data1.append(row)
    test_main=[]
    for j in xrange(len(data1)):
        k=np.array([[data1[j]]],dtype=np.float32).reshape(784,1)
        k/=256
        test_main.append(k)
    return [data_main,test_main]
        
class Network2(object):
    def __init__(self,sizes):
        self.sizes=sizes
        self.weight=[np.random.randn(y,x)/np.sqrt(x) for x,y in zip(sizes[:-1],sizes[1:])]
        self.bias=[np.random.randn(y,1) for y in sizes[1:]]
        self.activation=[]
        self.zs=[]
    #def sigmoid(z):
        #return 1.0/(1+np.exp(-z))
    def print1(self):
        print self.weight
    def set_activ(self,x):
        act=x
        #zs=[]
        self.activation=[x]
        for w,b in zip(self.weight,self.bias):
            z=np.dot(w,act)+b
            self.zs.append(z)
            act=sigmoid(z)
            self.activation.append(act)
        #print activation
    def backprop(self,x,y):
        self.set_activ(x)
        del_w=[np.zeros(w.shape) for w in self.weight]
        del_b=[np.zeros(b.shape) for b in self.bias]
        delta=(self.activation[-1]-y)
        del_b[-1]=delta
        del_w[-1]=np.dot(delta,self.activation[-2].transpose())
        for i in xrange(2,len(self.sizes)):
            sp=del_sigmoid(self.zs[-i])
            delta=np.dot(self.weight[-i+1].transpose(),delta)*sp
            del_w[-i]=np.dot(delta,self.activation[-i-1].transpose())
            del_b[-i]=delta
        return (del_w,del_b)
    def update(self,x,y,training,eta):
        #del_w,del_b=self.backprop(x,y)
        sum_del_w=[np.zeros(w.shape) for w in self.weight]
        sum_del_b=[np.zeros(b.shape) for b in self.bias]
        for x,y in training:
            #print y
            del_w,del_b=self.backprop(x,y)
            sum_del_w=[n+d for n,d in zip(sum_del_w,del_w)]
            sum_del_b=[i+j for i,j in zip(sum_del_b,del_b)]
            k=1.0-(eta*(0.5/1000))
        self.weight=[(k)*w-(eta/len(training)*delW) for w,delW in zip(self.weight,sum_del_w)]
        self.bias=[s-(eta/len(training)*delB) for s,delB in zip(self.bias,sum_del_b)]
    def final(self,training,test):
        #self.set_activ(x)
        #self.backprop(x,y)
        #print len(self.sizes)
        max=0
        eta1=1000.0/1024
        #print temp
        temp1=0
        flag=0
        for j in xrange(30):
            random.shuffle(training)
            mini_batch=[training[k:k+10] for k in xrange(0,len(training),10)]
            for mini in mini_batch:
                self.update(mini[:][0],mini[:][1],mini,eta1)
        #random.shuffle(test)
        result=[np.argmax(self.feed(c)) for c in test ]
        #for i in xrange(len(result)):
            #print i,
            #print ",",
            #print result[i]
        with open('E:\\Submission1.csv','wb') as csvfile:
            sub=csv.writer(csvfile,delimiter=',')
            sub.writerow(["ImageId"]+["Label"])
            for i in xrange(len(result)):
                sub.writerow([i+1]+[result[i]])
    def feed(self,x):
        for b,w in zip(self.bias,self.weight):
            x=sigmoid(np.dot(w,x)+b)
        return x
def sigmoid(z):
    return 1.0/(1+np.exp(-z))
def del_sigmoid(z):
    return sigmoid(z)*(1-sigmoid(z))

import mnist_loader
a,b,c=mnist_loader.load_data_wrapper()
k,l=data_loader()
new=Network2([784,30,10])
new.final(k,l)

