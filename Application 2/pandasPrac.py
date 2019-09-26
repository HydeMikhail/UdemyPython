#!/usr/bin/env python
'''
Udemy Python Class: Experimenting with Pandas
'''
import pandas
from geopy.geocoders import ArcGIS

NOM = ArcGIS()

F = "E:\\Documents\\Scripts\\Udemy Classes\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.csv"

DATAFRAME = pandas.read_csv \
    (F)
DATAFRAME["Address"] = DATAFRAME["Address"] + ", " + DATAFRAME["City"] + ", " + DATAFRAME["State"] + ", " + DATAFRAME["Country"]
DATAFRAME["Coordinates"] = DATAFRAME["Address"].apply(NOM.geocode)
DATAFRAME["Latitude"] = DATAFRAME["Coordinates"].apply(lambda x: x.latitude if x != None else None)
DATAFRAME["Longitude"] = DATAFRAME["Coordinates"].apply(lambda x: x.longitude if x != None else None)

print(DATAFRAME)

#Work: U:\\Documents\\GitCode\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.csv
#Home: E:\\Documents\\Scripts\\Udemy Classes\\UdemyPython\\Application 2\\PandasCSV\\supermarkets.csv
