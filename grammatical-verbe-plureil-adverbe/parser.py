import re
import sys
import in_put as ini
import output as out

output = '<texte>\n'

interogation = re.compile('[\?]+')
deuxPoints = re.compile('[\:]+')
exclamation = re.compile('[\!]+')
retourchariot = re.compile('[\n]+')
underscore = re.compile('[\_]+')
intermediate_punctuation = re.compile('[\,\;\"\-\n]+')
whites = re.compile('[\n\r\t ]+')
word_breaks = re.compile('[\n\r]+')
blanks_between_points = re.compile('(?<=[\!\?\.]) (?=[\!\?\.])')
ending_punctuation = re.compile('[\!\?]+')


def clean_text(text):
  
    text = intermediate_punctuation.sub('', text)
    text = retourchariot.sub(' ',text)
    text = exclamation.sub(' !\n', text)
    text = interogation.sub(' ?\n', text)
    text = deuxPoints.sub(':\n', text)
    text = blanks_between_points.sub(' ', text)
    return text

def split_to_sentence(text):
    ending_punctuation = re.compile('[\!]+')
    text = ending_punctuation.split(text)
    return text

def usage():
    print("<usage> main.py *.txt")
def main():
    if len(sys.argv) == 2:
        file = open(sys.argv[1], 'r')
        text = file.read()
        text = ini.prepare_output(text, output)
        txt = clean_text(text)
        phrases = split_to_sentence(txt)
        out.write_file(phrases)
        print("le dossier <<output_file>> est créé vous trouverez le fichier.xml dedans")
    else:
        usage()

if __name__ == '__main__':
    main()


exit(0)
