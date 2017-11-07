# -*- coding: utf-8 -*-

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
"class %%%(%%%):":
 "make a class named %%%  that is-a %%%. ",
"class %%%(object): \n\tdef __init__(self, ***)" :
 "class %%% has-a __init__ that makes self and *** parameters.",
"class %%%(object):\n\tdef ***(self, @@@)":
 "class %%% has-a fuction named *** that takes self and @@@ parameters" ,
"*** = %%%()":
 "set *** to an instance  of class %%%",
"***.***(@@@)":
 "from *** get the *** fuction, and call it with parameters self, @@@.",
"***.*** = '***'":
 "from *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english": #οταν θα τρεξουμε το προγραμμα πρεπει ν εχει 2 arguments το 2 να ειναι english kai to paw p sumplhrwsa sth prwth grammh gia na diavazei ta english
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from website
for word in urlopen(WORD_URL).readlines(): #auto ta diavazei t lexh
    WORDS.append(word.strip()) #etsi thn antigrafei


def convert(snippet,phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))] #dimiourgei t lista class names me tuxaies lexeis apo tis lista words p eisagame osa einai ta %%% tis listas snippet kai mallon kefalaia(apo to capitalize,)
    other_names = random.sample(WORDS, snippet.count("***")) #to idio me to panw apla osa einai ta *** tis listas (kai pali mallon kefalaia)
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")): # apo 0-osa stoixeia exei @@@ h lista snippet
        param_count = random.randint(1,3) #tuxaio noumero metaxu to 1 - 3  dld to 2 gt 2 einai se ka8e protash ta @@@
        param_names.append(', '.join(random.sample(WORDS,param_count))) #pairnei to stoixeio tuxaia ths words  kai ta vazei ena ena me , anamesa

    for sentence in snippet, phrase:
        result = sentence[:]


        for word in class_names:
            result = result.replace("***", word, 1)


        for word in other_names:
            result = result.replace("***", word, 1)


        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results



try:
    while True:
        snippets = PHRASES.keys() #bazei sth lista snippets ta keys apo to dictionary phrases (dld to prwto kommati mono)
        random.shuffle(snippets) #berdeuei ta stoixeia sth lista

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input(">")
            print "anwer: %s\n\n" %answer
except EOFError: "\nBye"
