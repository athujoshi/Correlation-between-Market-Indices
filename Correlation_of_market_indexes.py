#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 17:30:03 2018

@author: atharvajoshi
"""

import pandas as pd
import numpy as np
dataset = pd.read_csv('data_stocks.csv')

correlationmatrix=np.zeros((1,501))

for i in range(501): 
    x=dataset.iloc[:,[i+1]].values
    out2=[]
    for j in range(501):
        y=dataset.iloc[:,[j+1]].values
        exy=((np.transpose(x).dot(y))/41266)[0]
        ex=(np.mean(x,axis=0))[0]
        ey=(np.mean(y,axis=0))[0]
        cov=exy-(ex*ey)
        cov=cov[0]
        mx=(np.std(x,axis=0))[0]
        my=(np.std(y,axis=0))[0]
        corr=cov/(mx*my)
        out2.append(corr)
    out2=np.array([out2])
    correlationmatrix=np.vstack([correlationmatrix,out2])
    
correlationmatrix=np.delete(correlationmatrix, 0, 0)




