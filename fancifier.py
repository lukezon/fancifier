from random import randint
import re
import sys
sys.path.insert(0, '/home/lukezon/.local/lib/python2.7/site-packages')
from PyDictionary import PyDictionary
dictionary = PyDictionary()







def synonymreplacer(input):
    inputsplit = re.findall(r"[\w']+|[.,!?;:()]", input)
    output = ""
    for word in inputsplit:
        if word in [".",",","!","?",";",":","(",")"]:
            output = output + word
            #print("PUNCUATION")
        elif word in ["the","that","is","a","I","are","at","on","this","there","an"]:
            output = output + " " + word
        else:
            #print("DIRECT INPUT:")
            #print(word)
            synonyms = dictionary.synonym(word)
            #print synonyms
            if synonyms == None:
                output = output + " " + word
                #print(output)
            else:
                maxnum = len(synonyms)
                randomnumber = randint(0,maxnum-1)
                #print randomnumber
                synonymout = synonyms[randomnumber]
                #print(synonymout)
                output = output + " " + synonymout
                #print(output)
    return output


#input = input("Enter your text:")
#test = synonymreplacer(input)
#print(test)
