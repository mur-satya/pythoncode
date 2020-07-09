# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:05:29 2020

@author: MurthySatyavolu
"""


import pandas
df = pandas.read_csv('hrdata.txt', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('hrdata_modified.txt')