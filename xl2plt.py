# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:38:40 2020

@author: garci
"""
import numpy as np  
import matplotlib.pylab as plt
import xlwings as xw

# import the necessary packages
import argparse
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
'----------------------------------------------------------------------------------------'
ap.add_argument("-p", "--path", 
                default= [r'C:\[path]\[file].xlsx'],
                help="array with paths to datasets to plot")
'----------------------------------------------------------------------------------------'

ap.add_argument("-s", "--sheet", default='Sheet1', 
                help="name of sheet containing dataset")
ap.add_argument("-x", "--xcolumn", default='A1', 
                help="column with x data")
ap.add_argument("-y", "--ycolumn", default='B1', 
                help="column with y data")
args = vars(ap.parse_args())

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

def make():
    
    paths = args["path"]
    plt.style.use("ggplot")

    for path in paths:
        idx = args["sheet"]
        book=xw.Book(path)    
        x = book.sheets[idx].range( args["xcolumn"] + ':' + args["xcolumn"][0]+str(lastRow(idx,book)) ).value
        y = book.sheets[idx].range( args["ycolumn"] + ':' + args["ycolumn"][0]+str(lastRow(idx,book)) ).value
        plt.plot(x,y,label=path)
        book.close()
    plt.legend()
    
make()