
import output as out
import re


def check_input(status, text, input):
    if status == 0:
        if text == input:
            return 1
    if status == 1:
        if text[-3:] == input:
            return 1
    return 0


def les_infinitif(word):
    try:
        if word[-2:] == "er" or word[-2:] == "re" or word[-2:] == "ir" or word[-3] == "oir":
            return 1
    except IndexError as e:
        return 0

def split_to_word(text):
    separtion_punctuation = re.compile('[\s\']+')
    text = separtion_punctuation.split(text)
    return text


def open_file(file):
    file_ = open(file, 'r')
    content = file_.read()
    liste = split_to_word(content)
    file_.close()
    return liste

Propo = open_file("input_file/Propo.txt")
Pronoms_complements = open_file("input_file/Pronoms_complements.txt")
Pronom_indefinis = open_file("input_file/Pronom_indefinis.txt")
Pronom_personnel = open_file("input_file/Pronom_personnel.txt")
Pronom_possessifs = open_file("input_file/Pronom_possessifs.txt")
Pronom_demonstratif = open_file("input_file/Pronom_demonstratif.txt")
Pronom_relatifs = open_file("input_file/Pronom_relatifs.txt")
Negation = open_file("input_file/Negation.txt")
Liaisions = open_file("input_file/Liaisions.txt")
Gerondif = open_file("input_file/Gerondif.txt")

def init_input(texte):
    txt = split_to_word(texte)
    for i in range(len(txt)):
        if txt[i] in Pronoms_complements:
            if(check_input(0, txt[i-1].lower(), Propo)):
                txt[i] = "<article>"+txt[i]+"</article>"
            if (check_input(0, txt[i-1].lower(), Negation)):
                txt[i] = "<pronom>"+txt[i]+"</pronom>"
            elif (check_input(0, txt[i+1].lower(), Pronom_possessifs)):
                txt[i] = "<article>"+txt[i]+"</article>"
            elif (check_input(0, txt[i-1].lower(), Pronom_possessifs)):
                txt[i] = "<pronom>"+txt[i]+"</pronom>"
            elif (check_input(0, txt[i-1].lower(), Pronom_personnel)):
                txt[i] = "<pronom>"+txt[i]+"</pronom>"
            elif (check_input(0, txt[i+1].lower(), Pronom_demonstratif)):
                txt[i] = "<pronom>"+txt[i]+"</pronom>"
            elif (check_input(0, txt[i+1].lower(), Pronom_indefinis)):
                txt[i] = "<pronom>"+txt[i]+"</pronom>"
            elif (check_input(0, txt[i+1].lower(), Pronom_relatifs) or check_input(0, txt[i-1].lower(), Pronom_relatifs)):
                txt[i] = "<pronom>"+txt[i]+"</pronom>"
            elif (les_infinitif(txt[i+1].lower()) or les_infinitif(txt[i-1].lower())):
                txt[i] = "<pronom>"+txt[i]+"</pronom>"
            elif (check_input(0, txt[i-1].lower(), Liaisions)):
                txt[i] = "<article>"+txt[i]+"</article>"
            elif (check_input(0, txt[i-1].lower(), Propo) and check_input(0, txt[i+1].lower(), Propo)):
                txt[i-1], txt[i], txt[i+1], "</pronom>"
                txt[i]="<pronom>"+txt[i]+"</pronom>"
            elif (check_input(1, txt[i+1].lower(), Gerondif)):
                txt[i]="<article>"+txt[i]+"</article>"
            else:
                txt[i]="<article>"+txt[i]+"</article>"
    return txt
