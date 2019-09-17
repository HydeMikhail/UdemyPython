import os
import pandas

'''
dataFrame = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns = ["Col 1", "Col 2", "Col 3"], index = ["First", "Second"])
print(dataFrame)
'''

#Home File Location: "E:\\Documents\\Scripts\\Udemy Classes\\UdemyPython\\Application 2\\PandasCSV\\XXXXX"
#Work File Location: "U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\XXXXX"

dataFrame1 = pandas.read_csv("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.csv")
dataFrame2 = pandas.read_excel("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.xlsx", sheet_name = 0)
dataFrame3 = pandas.read_json("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.json")
dataFrame4 = pandas.read_csv("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets-commas.txt")
dataFrame5 = pandas.read_csv("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets-semi-colons.txt", sep = ";")
print(dataFrame1)
print("\n\n")
print(dataFrame2)
print("\n\n")
print(dataFrame3)
print("\n\n")
print(dataFrame4)
print("\n\n")
print(dataFrame5)