import json
from difflib import get_close_matches

#Consolidates json.load method into my own function.
def loadData(file):
    #Home File Location: "E:\\Documents\\Scripts\\Udemy Classes\\UdemyPython\\Application 1\\%s" % file
    #Work File Location: "U:\\Documents\\GitCode\\UdemyPython\\Application 1\\%s" % file
    return json.load(open("U:\\Documents\\GitCode\\UdemyPython\\Application 1\\%s" % file))

def formatting(defList):
    if type(defList) == list:
        for i in defList:
            print(i)
    else:
        print(defList)

#Returns the value of the dictionary given the key
def getDefinition(dictionary, word):
    return dictionary[word]

#Main function mimicking the C/C++ format. Creating a main function is not actually necessary. 
def main():
    
    print("\n\nWelcome to our dictionary! \nType in a word when prompted and the definition will be displayed on the screen!\n\n================================\nTo exit the program, enter \\end\n================================")
    dictionary = loadData("data.json")

    while True:

        print("\n")
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

    print("\nThanks for using the dictionary!")

main()