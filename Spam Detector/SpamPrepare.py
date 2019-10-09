# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 13:43:34 2017

@author: Vijay Vignesh
"""
import os
import nltk
from nltk.stem.porter import *
#os.chdir('E:\CourseraML\machine-learning-ex6\ex6')
file=open('emailSample1.txt','r')
load=file.read()
load=load.lower()
stemmer=PorterStemmer()
load=load.split()
#print(load)
load=[stemmer.stem(d) for d in load]
load=" ".join(load)
#print(load)
k1=re.compile(r"<+[^<>]+>")
load=k1.sub(" ",load)
k2=re.compile(r"(http|https)[\s]*")
load=k2.sub(" httpaddr ",load)
k3=re.compile(r"[0-9]+")
load=k3.sub(" number ",load)
k4=re.compile(r"[$]")
load=k4.sub(" dollar ",load)
k5=re.compile(r"[\t]")
load=k5.sub(" ",load)
k6=re.compile(r"[,._-]")
load=k6.sub(" ",load)
k7=re.compile(r"[\n]")
load=k7.sub(" ",load)
k8=re.compile(r"[\t]")
load=k8.sub(" ",load)
k9=re.compile(r"(\?|\!)")
load=k9.sub(" ",load)
file1=open('emailReady1.txt','w')
file1.write(load)