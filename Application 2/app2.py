#!/usr/bin/env python

'''
Application 2 of the Udemy Python Class
'''
import pandas
import folium
#from geopy.geocoders import ArcGIS

filePath = "E:\\Documents\\Scripts\\Udemy Classes\
\\UdemyPython\\Application 2\\app2-web-map\\Volcanoes.txt"

volcanoes = pandas.read_csv(filePath)

latLis = list(volcanoes["LAT"])
lonLis = list(volcanoes["LON"])
nameLis = list(volcanoes["NAME"])
elevLis = list(volcanoes["ELEV"])
statusLis = list(volcanoes["STATUS"])

def categorize(inElev, thresh):
    '''
    Determines Marker Color based on elevation
    '''
    if inElev < thresh:
        return "#0049FE"
    else:
        return "#FE2D00"

myMap = folium.Map(location=[latLis[int(len(latLis) / 2)], lonLis[int(len(lonLis) / 2)]], \
    zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name='My Map')

for lat, lon, nm, elev, status in zip(latLis, lonLis, nameLis, elevLis, statusLis):
    fg.add_child(folium.CircleMarker(location=[lat, lon], radius=7, \
        fill_color=categorize(elev, 2500), color="#000000", \
        popup=str(nm) + "\n" + str(elev) + "\n" + str(status)))
myMap.add_child(fg)
myMap.save("Map1.html")

#nom = ArcGIS()
#n = nom.geocode(input("Enter an address: "))
#coor = [n.latitude, n.longitude]
#myMap = folium.Map(location = [coor[0], coor[1]], zoom_start=10, tiles="Stamen Terrain")
#myMap.add_child(folium.Marker(location = [coor[0], coor[1]], \
# popup = str(coor[0]) + ", " + str(coor[1])))
#myMap.save("Map1.html")
