
import re
import sys,os
import in_put as ini
import output as out
points       = re.compile('[\.]+')
interogation = re.compile('[\?]+')
deuxPoints   = re.compile('[\:]+')
exclamation  = re.compile('[\!]+')
retourchariot = re.compile('[\n]+')
underscore    = re.compile('[\_]+')

def split_to_sentence(text):
    ending_punctuation = re.compile('[\!\?\.]+')
    text=ending_punctuation.split(text)
    return text

def clean_text(txt):
    txt = underscore.sub(' ',txt)
    txt = retourchariot.sub(' ',txt)
    txt = points.sub('.\n',txt)
    txt = exclamation.sub('!\n',txt)
    txt = interogation.sub('?\n',txt)
    txt = deuxPoints.sub(':\n',txt)
    return txt

def parser(txt):
    txt=clean_text(txt)
    phrases=split_to_sentence(txt)
    text_tagged=[]
    for x in phrases:
        if "l'" in x or "L'" in x or "la" in x or "les" in x or "Les" in x or "le" in x or "Le" in x:
            tagged = ini.init_input(x)
            for x in tagged:
                text_tagged.append(x+" ")
        else:
            text_tagged.append(x)    
    return text_tagged

def info():
	print("<info> python3 parseur.py + fichier .txt")

def main():
	if len(sys.argv)==2:
		file=open(sys.argv[1],'r')
		text=file.read()
		text = parser(text)
		out.write_file(text)
		print("le dossier <<output_file>> est créé vous trouverez le fichier.xml dedans")
	else:
		info()

if __name__ == '__main__':
	main()
