#!/use/bin/python3
import json

f = open('art.json',)

# returns JSON object as
# a dictionary

data = json.load(f)

for art in data:
    md = open('{0}.md'.format(art['slug']), 'w')
    print(md, "---")
    for (key, value) in art.items():
        if key in ['year', 'rasterWidth', 'rasterHeight']:
            print(md, '{0}: {1}'.format(key, int(value)))
        else:
            print(md, '{0}: "{1}"'.format(key, value))
    print(md, "---")
    md.close()


f.close()
