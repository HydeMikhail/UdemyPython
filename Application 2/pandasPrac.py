import os
import pandas
from geopy.geocoders import ArcGIS

#dataFrame = pandas.DataFrame(pandas.read_csv("E:\\Documents\\Scripts\\Udemy Classes\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.csv"))

nom = ArcGIS()
n = nom.geocode(input("Enter an address: "))
coor = [n.latitude, n.longitude]

print(coor)

