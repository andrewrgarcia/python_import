# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 12:39:28 2019

@author: garci
"""
import csv
import numpy as np
import matplotlib.pyplot as plt

'''.csv files in data folder'''
filename1,label1='example1.csv','Example 1'
filename2,label2='example2.csv','Example 2'


def conv( filename = 'name' ):


    '''if the csv file is in a subfolder to this script's, specify path'''
    fname_path='data/'

    with open(fname_path+filename, 'r') as f:
        X = list(csv.reader(f, delimiter=","))
    Xc=np.array(X[1:], dtype=np.float)

    x=Xc[:,0]
    y=Xc[:,1]

#    return Xc
    return x,y


'Read & Plot'
x,y = conv(filename1)
plt.plot(x,y,'k',label = label1)

x,y = conv(filename2)
plt.plot(x,y,label = label2)
plt.legend()
