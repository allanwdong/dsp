*Count Degrees*

import csv
import re
from collections import defaultdict

def count_degrees(csv_file_name):
    degrees = defaultdict(int)
    
    phd = re.compile('phd')
    scd = re.compile('scd')
    md = re.compile('md')
    mph = re.compile('mph')
    bsed = re.compile('bsed')
    ms = re.compile('ms')
    jd = re.compile('jd')
    zero = re.compile('0')
    ma = re.compile('ma')
    
    lst = [phd, scd, md, mph, bsed, ms, jd, zero, ma]
    dct= {phd : 'PhD', scd : 'ScD', md : 'MD', mph : 'MPH', 
          bsed : 'BSEd', ms : 'MS', jd : 'JD', zero: '0',
          ma : 'MA'}
    with open('faculty.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            x = list(row)[1].lower().replace('.', '')
            
            for i in lst:
                if i.search(x):
                    degrees[dct[i]] += 1
    degrees = dict(degrees)
    return degrees
                     
print(count_degrees('faculty.csv'))





*Sort Faculty by Last Name*

import csv

def get_dict():
    dct = {}
    with open('faculty.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lastname = row['name'].split(' ')[-1]
            value = [row[' degree'], 
                     row[' title'], 
                     row[' email']]

            if lastname in dct:
                dct.setdefault(lastname, [])
                dct[lastname].append(value)
            else:
                dct.setdefault(lastname, [])
                dct[lastname].append(value)
    return dct

answer = get_dict()
