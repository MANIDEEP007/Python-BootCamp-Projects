import json
from difflib import get_close_matches

#Read Json File
data = json.load(open("data.json"))

#Return Meaning of word if Exists
def translate(word):
    '''
    Check Key in Data. If it exists return meaning
    Else Return Not Exists. Check for Various possibilities
    (Upper Case / Capitalize / All Upper Case / Close Matches)
    of Typing
    '''
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))  > 0:
        choice = input("Is this word %s you are looking. If so press y: " % \
                       get_close_matches(word,data.keys())[0])
        if choice == 'y' or choice == 'Y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return word + " Word Not Exists"
    else:
        return word + " Word Not Exists"

#Get the Input from User    
word = input("Enter the word you want to get meaning: ")

#Get the Meaning of word
output = translate(word)

#If word have multiple meanings, Print each in seperate line
if type(output) == list:
    for each_meaning in output:
        print(each_meaning)

#Else Print the Meaning of word
else:
    print(output)
