from collections import OrderedDict
from itertools import islice
from os import mkdir
from openpyxl import load_workbook
import os

# load the workbook
wb = load_workbook('LA-ART-data.xlsx')
sheet = wb['Ark1']

# list to hold art
art_list = []

# Iterate through each row in worksheet and fetch values into dict

for row in islice(sheet.values, 1, sheet.max_row):
    art = OrderedDict()
    art['title'] = row[0]
    art['height'] = int(row[1]) if row[1] == int(row[1]) else row[1]
    art['width'] = int(row[2]) if row[2] == int(row[2]) else row[2]
    art['method'] = row[3]
    art['year'] = int(row[4])
    art['price'] = row[5] if isinstance(row[5], str) else int(row[5])
    art['rasterWidth'] = int(row[6])
    art['rasterHeight'] = int(row[7])
    art['fileName'] = row[8]
    art['medie'] = row[9]
    art['show'] = row[10]
    art['slug'] = row[11]
    art['weight'] = int(row[12])
    art_list.append(art)

os.mkdir('maleri')
os.mkdir('tegning')

for art in art_list:
#    prefix = 'm' if art['medie'] == 'maleri' else 't'
#    f = open('{0}-{1}.md'.format(prefix, art['slug']), 'w')
    os.mkdir(art['medie'] + '/' + art['slug'])
    f = open('{0}/{1}/index.md'.format(art['medie'], art['slug']), 'w')
    f.write("---\n")
    for (key, value) in art.items():
        if key in ['height', 'width', 'year', 'rasterWidth', 'rasterHeight']:
            f.write("{0}: {1}\n".format(key, value))
        else:
            f.write("{0}: \"{1}\"\n".format(key, value))
    f.write("---\n")
    f.close()

f = open('fiximages.sh', 'w')
f.write('#!/bin/sh' + "\n")
for art in art_list:
    f.write(('mv {0}/{2} {0}/{1}/'+"\n").format(art['medie'], art['slug'], art['fileName']))
f.close()
