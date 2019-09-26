import os
import pandas
from geopy.geocoders import ArcGIS

'''
dataFrame = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns = ["Col 1", "Col 2", "Col 3"], index = ["First", "Second"])
print(dataFrame)
'''
#dataFrame = pandas.DataFrame(pandas.read_csv("E:\\Documents\\Scripts\\Udemy Classes\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.csv"))

#Home File Location: "E:\\Documents\\Scripts\\Udemy Classes\\UdemyPython\\Application 2\\PandasCSV\\XXXXX"
#Work File Location: "U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\XXXXX"
nom = ArcGIS()
n = nom.geocode(input("Enter an address: "))
coor = [n.latitude, n.longitude]

print(coor)

'''
dataFrame1 = pandas.read_csv("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.csv")
dataFrame2 = pandas.read_excel("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.xlsx", sheet_name = 0)
dataFrame3 = pandas.read_json("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.json")
dataFrame4 = pandas.read_csv("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets-commas.txt")
dataFrame5 = pandas.read_csv("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets-semi-colons.txt", sep = ";")
print(coor)
'''

#print('''
#===================================
#Displaying DataFrames converted
#from various files using Pandas.
#The file type for each Data Frame
#is as follows:
#1:) CSV
#2:) XLSX
#3:) JSON
#4:) TXT by Commas
#5:) TXT by Semi Colons
#===================================
#''')

'''
print("Data Frame 1:\n\n" + str(dataFrame1))
print("\n\n")
print("Data Frame 2:\n\n" + str(dataFrame2))
print("\n\n")
print("Data Frame 3:\n\n" + str(dataFrame3))
print("\n\n")
print("Data Frame 4:\n\n" + str(dataFrame4))
print("\n\n")
print("Data Frame 5:\n\n" + str(dataFrame5)) 
'''