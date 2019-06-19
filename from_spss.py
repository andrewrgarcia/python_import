# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:21:28 2019

@author: garci
"""
'CONVERT SPSS FILES (.SAV) TO PYTHON DATAFRAME (LINE 12) PASS AS .CSV FILE (LINE 14)'

import pyreadstat
import pandas as pd

'FILE'
filename='experim.sav'
folder='data/'

df, meta = pyreadstat.read_sav(folder+filename)

'prints dataframe df'
print(df)

'converts .sav file to .csv and places it in script path'
df.to_csv( filename[:-4]+'.csv')