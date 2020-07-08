import csv

with open('employee.txt') as ding:
    dong = csv.reader(ding, delimiter='#')
    line_count = 0
    for row in dong:
        if line_count == 0:
           ## print(row[0],row[1],row[2])
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
           ## print(row[0],row[1],row[2])
            line_count += 1
    print(f'Processed {line_count} lines.')
