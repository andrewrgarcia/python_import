# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:49:38 2020

@author: garci
"""
'Extract y values at a certain x for all files in path'

import os
import pandas 
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", 
                default = r'C:\Users\..',
                type = str, help="path to csv files")
args = vars(ap.parse_args())


def readcsv(path,file):
    df = pandas.read_csv(path + file,header=20)  
    print(df)
#    
def make(path):
    
    asps = []
    for root, dirs, files in os.walk(path):
        for file in files:
            asps.append(file)
            readcsv(path,file)

#    print(asps)

make(args["path"])