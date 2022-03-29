import folium ## Library to use the interactive map
import webbrowser ## lIBRARY to open the brawser directly from the code
import pandas

## Read the data frame that contains all the coordinates of the volcanoes
data = pandas.read_csv("Volcanoes.txt") 


## Function for color depending of the heigh of the mountain
def color_heigh(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
## Assign variables to the latitude and longitud data in my data frame
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

## This is the map with its location and zoom
map = folium.Map(location =[39.3079189,-110.0597404], zoom_start= 5)

## Feature group (fg) is a group called My map
fgv = folium.FeatureGroup(name = 'Volcanoes')
fgp = folium.FeatureGroup(name = 'Population')

## I make the fg groups a 'child' of my object map 
map.add_child(fgv) 
map.add_child(fgp)
map.add_child(folium.LayerControl())

## Make a for loop using zip in order to use multiples variables to add multiple markers in the map
# in [[-25.3511836, -57.6478208],[-24.3511836, -58.6478208]]:  Just add here a comma and the position of the new marker 
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location =[lt, ln], radius = 6, popup = str(el) + " m", fill_color = color_heigh(el), color = 'grey', fill_opacity = 0.7, tooltip= 'Volcano'))

## Added a function that creates different colors depending on the population for the GeoJson file
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding= 'utf-8-sig').read(),
                            style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                                                    else 'orange' if 10000000 <= x['properties']['POP2005'] else 'red'}))

## Save the changes in the html file called Map1
map.save("Map1.html")

## With the webbrowser library I opened the html file
webbrowser.open_new_tab('Map1.html')
