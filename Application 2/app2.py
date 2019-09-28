#!/usr/bin/env python
import pandas
import folium
from geopy.geocoders import ArcGIS

volcanoes = pandas.read_csv("E:\\Documents\\Scripts\\Udemy Classes\\UdemyPython\\Application 2\\app2-web-map\\Volcanoes.txt")

latLis = list(volcanoes["LAT"])
lonLis = list(volcanoes["LON"])
nameLis = list(volcanoes["NAME"])
elevLis = list(volcanoes["ELEV"])
statusLis = list(volcanoes["STATUS"])

map = folium.Map(location = [latLis[int(len(latLis) / 2)], lonLis[int(len(lonLis) / 2)]], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name = 'My Map')

for lat, lon, nm, elev, status in zip(latLis, lonLis, nameLis, elevLis, statusLis):
    if status == "Historical":
        fg.add_child(folium.Marker(location = [lat, lon], popup = str(nm) + "\n" + str(elev) + "\n" + str(status), icon = folium.Icon(color = "red")))
    else:
        fg.add_child(folium.Marker(location = [lat, lon], popup = str(nm) + "\n" + str(elev) + "\n" + str(status), icon = folium.Icon(color = "blue")))

map.add_child(fg)
map.save("Map1.html")

'''
nom = ArcGIS()
n = nom.geocode(input("Enter an address: "))
coor = [n.latitude, n.longitude]
map = folium.Map(location = [coor[0], coor[1]], zoom_start=10, tiles="Stamen Terrain")
map.add_child(folium.Marker(location = [coor[0], coor[1]], popup = str(coor[0]) + ", " + str(coor[1])))
map.save("Map1.html")
'''