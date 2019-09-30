# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 15:06:45 2019

@author: garci
"""

import matplotlib.pyplot as plt
import numpy as np
import csv
import xlwings as xw
import pandas
import os

'''MAKE X-Y PLOTS WITH 2-COLUMN FILES
Andrew Garcia, 2019 '''


'''lastRow credit: answered Sep 14 '16 at 11:39  -  Stefan 
https://stackoverflow.com/questions/33418119/xlwings-function-to-find-the-last-row-with-data'''
def lastRow(idx, workbook, col=1):
    """ Find the last row in the worksheet that contains data.

    idx: Specifies the worksheet to select. Starts counting from zero.

    workbook: Specifies the workbook

    col: The column in which to look for the last cell containing data.
    """

    ws = workbook.sheets[idx]

    lwr_r_cell = ws.cells.last_cell      # lower right cell
    lwr_row = lwr_r_cell.row             # row of the lower right cell
    lwr_cell = ws.range((lwr_row, col))  # change to your specified column

    if lwr_cell.value is None:
        lwr_cell = lwr_cell.end('up')    # go up untill you hit a non-empty cell

    return lwr_cell.row


def readfile(path):
    asps = []
    for root, dirs, files in os.walk(path):
        for file in files:
            asps.append(file)
    
    print(asps)
    
    for file in asps:
        
        df= pandas.read_fwf(path+file,header=None)
        if df.shape[0] > 1 and df.shape[1] == 2:
            df.columns =['a', 'b'] 
            
            print(df)
            plt.figure()
    #        plt.plot(df[0],df[1])   
            plt.plot(df['a'],df['b'])
            plt.title(file)
            plt.xlabel('time  /  ps')
            plt.savefig(file+'.png')
#            plt.close()
#    return df


def readxl(path,file):

    book = xw.Book(path+file)
    
    x=book.sheets['Sheet1'].range('A1:A'+str(lastRow('Sheet1',book))).value
    y=book.sheets['Sheet1'].range('B1:B'+str(lastRow('Sheet1',book))).value
    
    plt.plot(x,y)
    plt.title(file[:-5])
    plt.xlabel('time  /  ps')
    plt.savefig(file+'.png')


#from proc_out_key import pathkey
#path = pathkey()


'''Process ALL tab-separated files in folder PATH (above) with two columns
(must be in a folder with tab-delimited files ONLY)'''
path = r'C:\Users\***\file_folder/'
readfile(path)
    

'''OR Process an Excel file(s) (specify the file name(s)) '''
path = r'C:\Users\***\file_folder/'
file = '*.xlsx'
readxl(path,file)