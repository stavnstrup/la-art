import json
from collections import OrderedDict
from itertools import islice
from openpyxl import load_workbook

# load the workbook
wb = load_workbook('LA-ART-data.xlsx')
sheet = wb['Ark1']

# list to hold art
art_list = []

# Iterate through each row in worksheet and fetch values into dict

for row in islice(sheet.values, 1, sheet.max_row):
    art = OrderedDict()
    art['title'] = row[0]
    art['height'] = row[1]
    art['width'] = row[2]
    art['method'] = row[3]
    art['year'] = row[4]
    art['price'] = row[5]
    art['rasterWidth'] = row[6]
    art['rasterHeight'] = row[7]
    art['fileName'] = row[8]
    art['type'] = row[9]
    art['show'] = row[10]
    art['slug'] = row[11]
    art_list.append(art)

    # Serialize the list if dicts to JSON
    j = json.dumps(art_list)

    # write to file
    with open('art.json', 'w') as f:
        f.write(j)
