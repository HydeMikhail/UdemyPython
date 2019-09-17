import os
import pandas

'''
dataFrame = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns = ["Col 1", "Col 2", "Col 3"], index = ["First", "Second"])
print(dataFrame)
'''

dataFrame1 = pandas.read_csv("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.csv")
dataFrame2 = pandas.read_excel("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.xlsx")
dataFrame3 = pandas.read_json("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.json")
print(dataFrame1)
print("\n\n")
print(dataFrame2)
print("\n\n")
print(dataFrame3)