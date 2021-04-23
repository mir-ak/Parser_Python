import re,os,sys

output = '<?xml version="1.0" encoding="utf-8"?>\n<?xml-stylesheet href="res.xsl" type="text/xsl"?>\n'
filename_end = re.compile('(?<=\w\.)txt$')

def write_file(txt):
    if not os.path.exists('output_file'):
        os.makedirs('output_file')
    with open(filename_end.sub('xml', 'output_file/texte.xml'), 'w') as xml_file:
        xml_file.write(output)
        for x in txt:
            xml_file.write(x)
        xml_file.write("\n</texte>")
   