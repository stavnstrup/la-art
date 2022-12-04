#!/usr/bin/python3

import csv
import os

# Run this script from the script directory

# Markdown path must end with /
markdownPath = '../content/'
# markdownPath = './demo/'

languages = ['da', 'en']

mediafiles = ['LA-ART-data - painting.csv',
         'LA-ART-data - drawing.csv', 
         'LA-ART-data - paperpainting.csv']

def validated(r):
   return ( str.isnumeric(r["id"]) and r["title"] and str.isnumeric(r["height"]) and
            str.isnumeric(r["width"]) and r["method"] and str.isnumeric(r["year"]) and
            str.isnumeric(r["price"]) and r["fileName"] and r["medie"] and r["draft"] and
            r["slug"] and str.isnumeric(r["order"]) )


for language in languages:
    print("Language: {}\n".format(language))
    lngPath = markdownPath + '/' + language
    os.makedirs(lngPath, exist_ok=True)
    os.makedirs(lngPath + '/' + 'painting', exist_ok=True)
    os.makedirs(lngPath + '/' + 'drawing', exist_ok=True)
    os.makedirs(lngPath + '/' + 'paperpainting', exist_ok=True)

    for media in mediafiles:
        print("Media: {}\n".format(media))
        with open(media, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0

            # Iterate through each row in worksheet and fetch values
            for row in csv_reader:
                print("{}\n".format(row["id"]))
                if line_count == 0:
                    line_count += 1
                os.makedirs(lngPath + '/' + row["medie"] + '/' + row["slug"], exist_ok=True)
                if (row["medie"] == 'painting' or row["medie"] == 'drawing' or row["medie"] == 'paperpainting') and row["slug"] != '':
                    f = open('{0}/{1}/{2}/index.md'.format(lngPath, row["medie"], row["slug"]), 'w')
                    f.write("---\n")
                    f.write('id: {0}\n'.format(row["id"]))
                    f.write('title: "{0}"\n'.format(row["title-" + language]))
                    f.write('height: {0}\n'.format(row["height"]))
                    f.write('width: {0}\n'.format(row["width"]))
                    f.write('method: "{0}"\n'.format(row["method-" + language]))
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
