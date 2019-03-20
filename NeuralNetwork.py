#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import functions
import matplotlib.pyplot as plt
import numpy as np

NumPoints=30

x1=np.random.randn(NumPoints,1)
y1=np.random.randn(NumPoints,1)
label1=np.zeros((NumPoints,1),dtype=int)

x2=1.3+np.random.randn(NumPoints,1)
y2=5.2+np.random.randn(NumPoints,1)
label2=np.ones((NumPoints,1),dtype=int)




#generate the data
set1=np.concatenate((x1,y1,label1),axis=1)
set2=np.concatenate((x2,y2,label2),axis=1)

data=np.concatenate((set1,set2),axis=0)

print data

#colours=np.concatenate( (np.zeros((2*NumPoints,1)) , 255*data[:,2] , np.zeros((2*NumPoints,1))) , axis=1 )

#print colours

plt.scatter(data[:,0], data[:,1],c=data[:,2],marker='o',edgecolors='none')

plt.legend(['class 1'])
plt.show()
