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


'''MAKE AN XY PLOT FOR A SINGLE EXCEL FILE (SPECIFY FOLDER PATH AND FILE NAME)'''
def readxl(path,file):

    book = xw.Book(path+file)
    
    x=book.sheets['Sheet1'].range('A1:A'+str(lastRow('Sheet1',book))).value
    y=book.sheets['Sheet1'].range('B1:B'+str(lastRow('Sheet1',book))).value
    book.close()
    plt.figure()
    plt.plot(x,y)
    plt.title(file[:-5])
    plt.xlabel('time')
    plt.savefig(file+'.png')
    
    
'''MAKE AN XY PLOT WITH TWO INDEPENDENT VARS (Y AND Z) FOR A SINGLE EXCEL FILE
  (SPECIFY FOLDER PATH AND FILE NAME)'''
def readxl2(path,file):

    book = xw.Book(path+file)
    
    x=book.sheets['Sheet1'].range('A1:A'+str(lastRow('Sheet1',book))).value
    y=book.sheets['Sheet1'].range('B1:B'+str(lastRow('Sheet1',book))).value
    z=book.sheets['Sheet1'].range('C1:C'+str(lastRow('Sheet1',book))).value

    book.close()
    plt.figure()
    plt.plot(x,y,label = r'y')
    plt.plot(x,z,label = r'z')

    plt.title(file[:-5])
    plt.xlabel('time')
    plt.savefig(file+'.png')
    plt.legend()



'MAKE XY PLOTS FOR ALL TAB DELIMITED FILES IN A FOLDER (SPECIFY FOLDER PATH)'
def writetab_bulk(path):
    asps = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith('.xlsx') and not file.endswith('.csv')\
            and not file.endswith('.png') and not file.endswith('.txt')\
            and not file.endswith('.xls'):
                asps.append(file)
    print(asps)
    
    index=1
    for file in asps:
        df= pandas.read_fwf(path+file,header=None,infer_nrows=10000)
        xdim, ydim = df.shape[0], df.shape[1]
        
        if xdim > 1 and ydim == 2:
            df.columns =['a','b'] 
            
            print(file,index)
#            print(df)
            plt.figure()
            plt.plot(df['a'],df['b'])
            plt.title(file)
            plt.xlabel('time  /  ps')
            plt.savefig(file+'.png')
#            plt.close()
            index+=1
#            return df
  
'(optional): create function with directory path (keep uncommented if unaware)'
#from proc_out_key import pathkey
#path = pathkey()  


'''COMMAND SECTION (INPUT)'''

'MAKE XY PLOTS FOR ALL TAB DELIMITED FILES IN A FOLDER (SPECIFY FOLDER PATH)'
path = r'C:\Users\***\file_folder/'
df=writetab_bulk(path)

'''MAKE AN XY PLOT FOR A SINGLE EXCEL FILE (SPECIFY FOLDER PATH AND FILE NAME)'''
#path = r'C:\Users\***\file_folder/'
#file = '**.xlsx'
#writexl(path,file)