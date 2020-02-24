# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:49:38 2020

@author: garci
"""
'Extract y values at a certain x for all files in path'

import os
import pandas 
import argparse
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", 
                default = r'C:\Users\garci\...\folder/',
                type = str, help="path to csv files")
ap.add_argument("-r", "--reference_column", 
                default = "Wavelength",
                type = str, help="name of reference column for indexing")
ap.add_argument("-i", "--indexed_column", 
                default = "Abs",
                type = str, help="name of column which is indexed based on reference column")
ap.add_argument("-c", "--string_cutoff", 
                default = "M",
                type = str, help="if file name contains the x-value up to a certain string character\
                this cutoff will define where the x-value (float) will end (e.g. file = 5001.45Go.csv with \
                -c G will give 5001.45")
ap.add_argument("-l", "--lookup_value", 
                default = 555,
                type = float, help="lookup value for reference column")
args = vars(ap.parse_args())


def readcsv(path,file):
    df = pandas.read_csv(path + file,header=15)  
    df = df.set_index(args["reference_column"])
    y = df[args["indexed_column"]].loc[args["lookup_value"]]
#    print(df)
    return y
#    
def make(path):
   
    x=[]
    y= []
    asps = []
    for root, dirs, files in os.walk(path):
        for file in files:
            asps.append(file)
            if args["string_cutoff"] is not "***":
                x.append(float(file.split(args["string_cutoff"])[0])) 
            else:
                x.append(float(file)) 
            y.append(readcsv(path,file))
#            print(readcsv(path,file))
            
    plt.plot(x,y)
    print('x : {} \n y: {}'.\
         format(x,y))


make(args["path"])