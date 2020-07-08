# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:25:55 2020

@author: MurthySatyavolu
"""


import csv

with open('emp2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
    
    
with open('emp2.csv', mode='r') as cfile:
    creader = csv.DictReader(cfile)
    line_count = 0
    for row in creader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["emp_name"]} works in the {row["dept"]} department, and was born in {row["birth_month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')