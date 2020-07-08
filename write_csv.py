# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:18:41 2020

@author: MurthySatyavolu

"""

import csv

with open('emp.csv', mode='w') as employee_file:
    emp_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    emp_writer.writerow(['name','department','birthday'])
    emp_writer.writerow(['John ', 'Accounting', 'November'])
    emp_writer.writerow(['Jillian', 'IT', 'March'])


