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


def readxl(path,file):

    book = xw.Book(path+file)
    
    x=book.sheets['Sheet1'].range('A1:A'+str(lastRow('Sheet1',book))).value
    y=book.sheets['Sheet1'].range('B1:B'+str(lastRow('Sheet1',book))).value
    
    plt.plot(x,y)
    plt.title(file[:-5])
    plt.xlabel('time  /  ps')
    plt.savefig(file+'.png')
      

'''SPECIFIC EXCEL FILE '''
path = r'C:\Users\***\file_folder/'
file = '*.xlsx'
readxl(path,file)