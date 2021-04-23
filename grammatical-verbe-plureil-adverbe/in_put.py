
import re


def adverbe(word):
    if word[-4:] == "ment":
        return 1
    return 0


def split_to_word(text):
    separtion_punctuation = re.compile('[\s]+')
    text = separtion_punctuation.split(text)
    return text


def open_file(file):
    file_ = open(file, 'r')
    content = file_.read()
    liste = split_to_word(content)
    file_.close()
    return liste


Pluriels = open_file("input_file/Pluriels.txt")
Pronom_personnel = open_file("input_file/Pronom_personnel.txt")
Determinant = open_file("input_file/Determinant.txt")
Pronom_personnel_negatif = open_file("input_file/Pronom_personnel_Neg.txt")
agreement = ["arrangement"]


def prepare_output(splitted_txt, output):
    tmp = ''
    word = split_to_word(splitted_txt)
    for i in range(len(word)):
        if word[i].lower() in Pronom_personnel:
            #if word[i+1]
            if word[i+1].lower() == 'y' or word[i+1].lower() == "n'y" or word[i+1].lower() == 'lui' or word[i+1].lower() == 'se' :
                output += word[i] + ' '
                i += 1
            if  word[i+1].lower() == 'une' or word[i+1].lower() == 'me' or  word[i+1].lower() == 'ne' or word[i+1].lower() == 'le' or word[i+1].lower() == "l'a"  :
                output += word[i] + ' '
                i = i +1 
            output += word[i] + ' <verbe>' + word[i+1] + '</verbe> '
            tmp = word[i+1]
        elif word[i].lower() in Pluriels:
            output += word[i] + ' <pluriel>' + word[i+1] + '</pluriel> '
            tmp = word[i+1]
        elif (adverbe(word[i].lower())):
            if not(word[i-1].lower() in Determinant):
                output += '<advrebe>' + word[i] + '</advrebe> '
            else:
                output += word[i]+' '
        elif tmp == word[i]:
            continue
        else:
            if word[i].lower() == 'y' or word[i].lower() == "n'y" or word[i].lower() == 'lui' or word[i].lower() == 'se ':
                i += 1
            elif  word[i].lower() == 'une' or word[i].lower() == 'me' or word[i].lower() == 'ne' or word[i].lower() == 'le' or word[i].lower() == "l'a" :
                i += 1
            else:
                output += word[i]+' '
    return output
