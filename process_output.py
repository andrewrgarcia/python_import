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
            if not file.endswith('.xlsx') and not file.endswith('.csv')\
            and not file.endswith('.png') and not file.endswith('.txt')\
            and not file.endswith('.xls'):
                asps.append(file)
    print(asps)
    
    'conditional (quick fix for fwf number-cutting problem):'
    def num_cut_sol(var,c_num,tol):
        cut_num = c_num
        i, k, prev = 0,0,-1
        while i < xdim:
            curr = df[var][i]%cut_num
#            print(curr,prev)
            if curr*tol < prev:
                k+=1
            df[var][i]+=k*cut_num
            prev = df[var][i]%cut_num
            i+=1
       
    index=1
    for file in asps:
        df= pandas.read_fwf(path+file,header=None)
        xdim, ydim = df.shape[0], df.shape[1]
        
        if xdim > 1 and ydim == 2:
            df.columns =['a','b'] 
            '''-TEST: must turn off 'b' to figure out y-axis number cut 
            (c_num) and tolerance. then turn on with appropriate values------'''
            num_cut_sol('a',100,1)
            num_cut_sol('b',10000,10)
            '''--------------------------------------------------------------'''
            
            print(file,index)
#            print(df)
            plt.figure()
    #        plt.plot(df[0],df[1])   
            plt.plot(df['a'],df['b'])
            plt.title(file)
            plt.xlabel('time  /  ps')
            plt.savefig(file+'.png')
#            plt.close()
            index+=1
#            return df


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


'''BROKEN // TRYING TO FIX: 
ALL TAB/SPACE-DELIMITED FILES IN FOLDER PATH '''
#path = r'C:\Users\***\file_folder/'
#df=readfile(path)
    

'''SPECIFIC EXCEL FILE '''
path = r'C:\Users\***\file_folder/'
file = '*.xlsx'
readxl(path,file)