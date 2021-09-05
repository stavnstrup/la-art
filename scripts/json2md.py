#!/use/bin/python3
import json

f = open('art.json',)

# returns JSON object as
# a dictionary

data = json.load(f)

for art in data:
    md = open('{0}.md'.format(art['slug']), 'w')
    md.write("---\n")
    for (key, value) in art.items():
        if key in ['year', 'rasterWidth', 'rasterHeight']:
            md.write("{0}: {1}\n".format(key, int(value)))
        else:
            md.write("{0}: \"{1}\"\n".format(key, value))
    md.write("---\n")
    md.close()

f.close()
