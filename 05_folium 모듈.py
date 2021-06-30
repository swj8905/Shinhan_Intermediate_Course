# import folium as f
from folium import Map

map = Map(location=[37.497, 127.027], zoom_start=17)
map.save("./map.html")