import os
import pandas
from geopy.geocoders import ArcGIS

nom = ArcGIS()

dataFrame = pandas.read_csv("U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.csv")
dataFrame["Address"] = dataFrame["Address"] + ", " + dataFrame["City"] + ", " + dataFrame["State"] + ", " + dataFrame["Country"]
dataFrame["Coordinates"] = dataFrame["Address"].apply(nom.geocode)
dataFrame["Latitude"] = dataFrame["Coordinates"].apply(lambda x: x.latitude if x != None else None)
dataFrame["Longitude"] = dataFrame["Coordinates"].apply(lambda x: x.longitude if x != None else None)

print(dataFrame)