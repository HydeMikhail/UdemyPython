import json
from difflib import get_close_matches

#Consolidates json.load method into my own function.
def loadData(file):
    #Home File Location: "E:\\Documents\\Scripts\\Udemy Classes\\UdemyPython\\Application 1\\%s" % file
    #Work File Location: "U:\\Documents\\GitCode\\UdemyPython\\Application 1\\%s" % file
    return json.load(open("E:\\Documents\\Scripts\\Udemy Classes\\UdemyPython\\Application 1\\%s" % file))

def formatting(defList):
    if type(defList) == list:
        for i in defList:
            print("\n" + str(i) + "\n")
    else:
        print("\n" + str(defList) + "\n")

#Returns the value of the dictionary given the key
def getDefinition(dictionary, word):
    return dictionary[word]

#Main function mimicking the C/C++ format. Creating a main function is not actually necessary. 
def main():
    
    print('''
==========================
Welcome to our dictionary!
==========================

================================
Enter a word in the command line
and the program will return it's 
definition to you. If your entry
is misspelled the software will 
suggest the closest match.
    
To exit the program, enter \\end
================================
''')

    dictionary = loadData("data.json")

    while True:

        usrInput = str(input("Enter word: ")).lower()

        if usrInput == "\\end":
            break
        elif usrInput in dictionary:
            defList = (getDefinition(dictionary, usrInput))
            formatting(defList)
        elif usrInput.title() in dictionary:
            defList = (getDefinition(dictionary, usrInput.title()))
            formatting(defList)
        elif usrInput.upper() in dictionary:
            defList = (getDefinition(dictionary, usrInput.upper()))
            formatting(defList)
        elif len(get_close_matches(usrInput, dictionary.keys())) > 0:
            print("Did you mean %s instead?" % get_close_matches(usrInput, dictionary.keys())[0])
            usrChoice = input("Enter yes [y] or no [n]: ").lower()
            if usrChoice == "y":
                x = (getDefinition(dictionary, get_close_matches(usrInput, dictionary.keys())[0]))
                formatting(x)
            else:
                print("Entry no recognized. Please try again.")

    print('''
================================

Thanks for using the dictionary!
   
================================
    ''')

main() 