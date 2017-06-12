





Sort Faculty by Last Name
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
