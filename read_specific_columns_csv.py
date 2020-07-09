# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:08:51 2020

@author: MurthySatyavolu
"""

import csv

with open('example.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    # now, remember our lists?

    whatColor = input('What color do you wish to know the date of?:')
    coldex = colors.index(whatColor)
    print(coldex)
    theDate = dates[coldex]
    print('The date of',whatColor,'is:',theDate)
    
#1/2/2014,5,8,red
#1/3/2014,5,2,green
#1/4/2014,9,1,blue