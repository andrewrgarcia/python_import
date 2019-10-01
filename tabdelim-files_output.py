# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:14:32 2019

@author: garci
"""

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
            
    def num_cut_sol2(var,tol):
        i, k, prev = 0,0,-1
        avgmdif=100
        while i < xdim:
            curr = df[var][i]
            mdif0 = abs(curr-prev)
            if i > 200:
                if mdif0 > tol*avgmdif:
                    print(mdif0,avgmdif)
                    df[var][i:]+=mdif0
                    print(df[var][i])
            prev = df[var][i]
            mdif = abs(curr-prev)
            avgmdif=np.mean([mdif0,mdif,avgmdif])
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
            num_cut_sol2('b',50)
            '''------------------------------------------------------------'''
            
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
            
            
'''BROKEN // TRYING TO FIX: 
ALL TAB/SPACE-DELIMITED FILES IN FOLDER PATH '''
#path = r'C:\Users\***\file_folder/'
df=readfile(path)