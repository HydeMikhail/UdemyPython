import json

'''
A test to work with VIM editor
'''

def loadData(file):
    #Home File Location: "E:\\Documents\\Scripts\\Python Mega Course\\Application 1\\%s" % file
    #Work File Location: "U:\\Documents\\GitCode\\UdemyPython\\Application 1\\%s" % file
    return json.load(open("U:\\Documents\\GitCode\\UdemyPython\\Application 1\\%s" % file))

def getDefinition(dictionary, word):
    return dictionary[word]

def main():
    dictionary = loadData("data.json")
    while True:
        usrInput = str(input("Enter word: ")).lower()
        if usrInput == "\\end":
            break
        elif usrInput in dictionary:
            print(getDefinition(dictionary, usrInput))
        else:
            print("Word not recognized. Try again.")
    print("Thanks for using the dictionary!")

main()