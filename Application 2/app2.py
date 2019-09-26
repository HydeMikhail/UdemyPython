#!/usr/bin/env python
import folium
from geopy.geocoders import ArcGIS

nom = ArcGIS()
coor = input("Enter an address: ")
n = nom.geocode(coor)

map = folium.Map(location = [n.latitude, n.longitude], zoom_start=6, tiles="Stamen Terrain")
map.add_child(folium.Marker(location = [n.latitude, n.longitude], popup = coor))
map.save("Map1.html")