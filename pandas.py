# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:58:04 2020

@author: MurthySatyavolu
"""


import pandas
##df = pandas.read_csv('hrdata.txt')
df = pandas.read_csv('hrdata.txt', index_col='Name', parse_dates=['Hire Date'])
print(df)

df = pandas.read_csv('hrdata.txt', 
            index_col='Employee', 
            parse_dates=['Hired'], 
            header=0, 
            names=['Employee', 'Hired','Salary', 'Sick Days'])
print(df)