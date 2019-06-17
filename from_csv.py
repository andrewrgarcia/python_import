# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 12:39:28 2019

@author: garci
"""
import csv
import numpy as np
import matplotlib.pyplot as plt


def data( filename = 'name' ):
    
    
    '''if the csv file is in a subfolder to this script's, specify path'''
    fname_path='data/'
    
    with open(fname_path+filename, 'r') as f:
        X = list(csv.reader(f, delimiter=","))        
    Xc=np.array(X[1:], dtype=np.float)        

    x=Xc[:,0]
    y=Xc[:,1]
    
#    return Xc
    return x,y



x,y = data('33as.csv')
plt.plot(-x,y,'k',label = 'MIL-53-33as')

x,y = data('33sc.csv')
plt.plot(-x,y,label = 'MIL-53-33sc')
plt.legend()


