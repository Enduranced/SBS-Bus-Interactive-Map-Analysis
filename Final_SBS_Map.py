from urllib.request import urlopen
import json
import pandas as pd
import plotly.graph_objects as go

file = urlopen('https://raw.githubusercontent.com/Enduranced/SBS-Bus-Interactive-Map-Analysis/main/Data/Singaporemap.txt')
counties = json.load(file)
### Setting up data for matching purposes (Orignally on token mode) ###
for i in counties['features']:
        i['id']=i['properties']['PLN_AREA_N']
#####################   DataFrames  ############################
df1 = pd.read_csv("https://raw.githubusercontent.com/Enduranced/SBS-Bus-Interactive-Map-Analysis/main/Data/SingaporePopDistri.csv")
df2 = pd.read_csv("https://raw.githubusercontent.com/Enduranced/SBS-Bus-Interactive-Map-Analysis/main/Data/Infowithcoordinates.csv")

import plotly.express as px
mi = min(df1['Buses that stop at the busstop'])
ma = max(df1['Buses that stop at the busstop'])

fig = px.choropleth_mapbox(df1, geojson=counties, locations='Location', color='Buses that stop at the busstop',
                           color_continuous_scale="Greys",
                           range_color=(mi, ma),
                           mapbox_style="carto-positron",
                           center = {"lat": 1.3521, "lon": 103.8198},
                           labels = "Population Distribution"
                          )


fig.add_scattermapbox(lat = df2.lad , lon = df2.lon, mode = 'markers', marker = go.scattermapbox.Marker(
             size = df2.Number+1, color ="orange", sizemode = "diameter"),  name = "Buses that stop at the busstop",
             hovertext= "Number of buses that stops: " + df2.Number.astype(str))
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
))

fig.update_layout(title_text ='Singapore Bus Map (SBS)', mapbox_zoom=9.5, showlegend=True)

fig.add_scattermapbox()
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()