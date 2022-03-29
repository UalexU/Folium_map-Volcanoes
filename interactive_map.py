
from email.encoders import encode_noop
from turtle import fillcolor
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

## Fg is a group called My map
fg = folium.FeatureGroup(name = 'My map')

map.add_child(fg) ## I make the fg group a 'child' of my object map 

tooltip = "Volcano" # This is the text that appears when my cursor is over the marker

## Make a for loop using zip in order to use multiples variables to add multiple markers in the map
# Alternative for loop for coordinates in [[-25.3511836, -57.6478208],[-24.3511836, -58.6478208]]:  Just add here a comma and the position of the new marker 
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location =[lt, ln], radius = 6, popup = str(el) + " m", fill_color = color_heigh(el), color = 'grey', fill_opacity = 0.7, tooltip= tooltip))

fg.add_child(folium.GeoJson(data = (open('world.json', 'r', encoding= 'utf-8-sig').read())))

## Save the changes in the html file called Map1
map.save("Map1.html")

## With the webbrowser library I opened the html file
webbrowser.open_new_tab('Map1.html')

## Green https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcy0XzzRhL8QxbBcRH7LIiWm7oSTbFdoZ998ZfLTz3d_6SY2f1Ir3svrjC_aF9TBYrRjM&usqp=CAU
## https://www.google.com/imgres?imgurl=https%3A%2F%2Fthumbs.dreamstime.com%2Fb%2Fvolcano-erupting-icon-green-volcano-erupting-icon-white-isolated-green-background-vector-illustration-102013670.jpg&imgrefurl=https%3A%2F%2Fwww.dreamstime.com%2Fvolcano-erupting-icon-green-volcano-erupting-icon-white-isolated-green-background-vector-illustration-image102013670&tbnid=hvVTLm8ZGhKh0M&vet=12ahUKEwi6rKHo7-n2AhWIspUCHUN_BFMQMygBegUIARDQAQ..i&docid=hYXI6h2LPIxtaM&w=800&h=800&q=volcano%20green%20icon&ved=2ahUKEwi6rKHo7-n2AhWIspUCHUN_BFMQMygBegUIARDQAQ
## Red https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn-icons-png.flaticon.com%2F512%2F191%2F191022.png&imgrefurl=https%3A%2F%2Fwww.flaticon.com%2Ffree-icon%2Fvolcano_191022&tbnid=iWFLsvVhYHNWwM&vet=12ahUKEwiYnIb-7-n2AhWQgpUCHe6iCmcQMygEegUIARDKAQ..i&docid=_ju_UyNM2Pe70M&w=512&h=512&q=volcano%20red%20icon&ved=2ahUKEwiYnIb-7-n2AhWQgpUCHe6iCmcQMygEegUIARDKAQ
## Yellow data:image/png;base64,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 
