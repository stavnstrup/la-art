#!/usr/bin/python3

import csv
import os

# Run this script from the script directory

# Markdown path must end with /
# markdownPath = './'
markdownPath = '../content/dk/'

def validated(r):
   return ( str.isnumeric(r["id"]) and r["title"] and str.isnumeric(r["height"]) and
            str.isnumeric(r["width"]) and r["method"] and str.isnumeric(r["year"]) and
            str.isnumeric(r["price"]) and r["fileName"] and r["medie"] and r["draft"] and
            r["slug"] and str.isnumeric(r["order"]) )


with open('LA-ART-data - maleri.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    os.makedirs(markdownPath + 'maleri', exist_ok=True)
    os.makedirs(markdownPath + 'tegning', exist_ok=True)

    # Iterate through each row in worksheet and fetch values
    for row in csv_reader:
#        print(row)
        if line_count == 0:
#            print(f'Column names are {", ".join(row)}')
            line_count += 1
        os.makedirs(markdownPath + row["medie"] + '/' + row["slug"], exist_ok=True)
        if (row["medie"] == 'maleri' or row["medie"] == 'tegning') and row["slug"] != '' and row["draft"] == 'no':
            f = open('{0}{1}/{2}/index.md'.format(markdownPath, row["medie"], row["slug"]), 'w')
            f.write("---\n")
            f.write('id: {0}\n'.format(row["id"]))
            f.write('title: "{0}"\n'.format(row["title"]))
            f.write('height: {0}\n'.format(row["height"]))
            f.write('width: {0}\n'.format(row["width"]))
            f.write('method: "{0}"\n'.format(row["method"]))
            f.write('year: {0}\n'.format(row["year"]))
            f.write('price: "{0}"\n'.format(row["price"]))
            f.write('fileName: "{0}"\n'.format(row["fileName"]))
            f.write('medie: "{0}"\n'.format(row["medie"]))
            f.write('draft: "{0}"\n'.format(row["draft"]))
            f.write('slug: "{0}"\n'.format(row["slug"]))
            f.write('weight: "{0}"\n'.format(row["order"]))
            f.write("---\n")
            f.close()

#            print(f'{row["title"]} {0}'.format(validated(row)))
