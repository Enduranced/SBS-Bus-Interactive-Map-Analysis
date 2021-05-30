import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
df = pd.read_csv(r'C:\Users\spenc\Documents\python\Busstops\Infowithcoordinates.csv')
file = open(r'C:\Users\spenc\Documents\python\Busstops\Singaporebusstops.txt')
map = json.load(file)
px.set_mapbox_access_token("pk.eyJ1Ijoic3BlbmNlcm5nIiwiYSI6ImNrb3pnYnpqZjBqZ3kydnFpODd5bjVjYjEifQ.e0xsqpx9jY-9zrlPUEeuog")
fig = px.scatter_mapbox(df, lat = 'lad', lon = 'lon', color = 'Number', color_continuous_scale = px.colors.cyclical.HSV, 
size_max =44 )
# Putting in pop data
df2 = pd.read_csv(r'\Users\spenc\Documents\python\Busstops\SingaporeHousingDistri.csv')
file2 = open(r'C:\Users\spenc\Documents\python\Busstops\55Singaporemap.txt')
map2 = json.load(file2)
fig.update_layout(df2, geo = map2, locations= 'Location')



# fig.update_layout(
#     mapbox = {
#         'style': "stamen-terrain",
#         'zoom': 12, 'layers': [{
#             'source': {
#                 'type': "FeatureCollection",
#                 'features': [{
#                     'type': "Feature",
#                     'geometry': {
#                         'type': "MultiPolygon",
#                         'coordinates': [[[103.8515644182791,1.269263145564809],
#                         [103.85156581997522,1.268105448048998],
#                         [103.8515706227875,1.264140650370849],
#                         [103.85066952401387,1.263041793395822],
#                         [103.85076015827286,1.262940725472663],
#                         [103.85205661108235,1.261495060876852],
#                         [103.85117376272979,1.260737807005563],
#                         [103.84570064866521,1.266837084778484],
#                         [103.84428335141818,1.265540819585711],
#                         [103.84672236649223,1.26244768069595],
#                         [103.84599028332318,1.261558603105413],
#                         [103.83945066133339,1.267618475885683],
#                         [103.832081073957,1.267414261853566],
#                         [103.82464004985596,1.263157582112706],
#                         [103.82411838839661,1.263084566391367],
#                         [103.82440711369726,1.26019361616417],
#                         [103.83042136974039,1.263628070226219],
#                         [103.83619422095336,1.263810155144295],
#                         [103.84247597686698,1.257898522227992],
#                         [103.83636903798954,1.254810076359961],
#                         [103.83126396873429,1.256419860780553],
#                         [103.82932497036947,1.256792446082765],
#                         [103.82681144467466,1.257663833835945],
#                         [103.82484272631417,1.259013858914698],
#                         [103.82401119190077,1.258232236827986],
#                         [103.8236446330146,1.258417616760839],
#                         [103.82346731845874,1.258507290220551],
#                         [103.8232017895788,1.258641575654089],
#                         [103.82339836629106,1.260835013517848],
#                         [103.82325054746626,1.263073196184547],[103.81990718751074,1.263090051896836],[103.81581633477123,1.263826215784535],[103.8150524991176,1.264409173217063],[103.81154529802228,1.262723156406892],[103.81033318308056,1.26321438791899],[103.81147543776225,1.264801115262295],[103.8122386245974,1.264784219036011],[103.81324069432281,1.263728516554515],[103.81493865431909,1.264511943542947],[103.8128432057725,1.266403532832058],[103.81119056422361,1.266395602343969],[103.80988533566779,1.265232664261313],[103.80826696340775,1.265103948856305],[103.80721789258372,1.2658815557446],[103.80552684732497,1.263756253298987],[103.80514180780642,1.262298863188944],[103.80100080433658,1.265889241068316],[103.80129864314561,1.266451373592701],[103.79921008684279,1.268201638266673],[103.80157548701483,1.272309946771641],[103.80220905305227,1.272694178475821],[103.80196303673048,1.274926932017635],[103.8031278917418,1.278930457043859],[103.80130346242376,1.282778752080138],[103.80161906880836,1.284163608921509],[103.80318752126618,1.286771776255656],[103.80506705800141,1.28800425176575],[103.8088744026396,1.292387077401719],[103.80957872142153,1.292480209283129],[103.81536376183975,1.291522668609804],[103.815976656856,1.294106058810527],[103.82161689309346,1.293571887556041],[103.82438878635571,1.291930300369257],[103.82610573998436,1.292425104678634],[103.82859709543314,1.292719790635833],[103.83104483524923,1.292080066239505],[103.83180553925254,1.292154761925635],[103.83342776653737,1.292369546326927],[103.83491673031091,1.289579350508367],[103.83500221153854,1.287269366497246],[103.83475827317226,1.285854846795146],[103.83548521013135,1.283821776988832],[103.83641294546089,1.282871529063424],[103.83924168432056,1.28079201197501],[103.84059677693187,1.277547174182557],[103.84137181578335,1.274154612189558],[103.84215451704763,1.27258899013923],[103.84513928020594,1.272620411143023],[103.8477789167942,1.271672646648407],[103.8515644182791,1.269263145564809]]]
#                     }
#                 }]
#             },
#             'type': "fill", 'below': "traces", 'color': "royalblue"}]},
#     margin = {'l':0, 'r':0, 'b':0, 't':0})




fig.show()













# maxval = df['Buspasses'].max()
# minval = df['Buspasses'].min()
# fig = go.Figure(go.Choroplethmapbox( 
#     geojson = map, 
#     featureidkey = 'id',
#     locations = df.id,
#     z = df.Number,
#     zauto = True, 
#     colorscale = 'viridis',
#     marker_opacity =0.8, 
#     marker_line_width = 0.8, 
#     showscale  =True,
# ))

# fig.update_layout(
#         title = 'Bus Routes in Singapore',
#         mapbox_style = 'carto-darkmatter',
#         mapbox_zoom =10,
#         mapbox_center = {"lat": 1.3521 , "lon":103.8198}
#     )
# fig.show()

# fig = px.choropleth_mapbox(df, locations ='id', geojson = busstops, color = 'Buspasses',
#                            range_color = (minval,maxval),

#                            mapbox_style="carto-positron",
#                            center = {'lat':1.3521, 'lon':103.8198},zoom=10)

# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()







#import plotly.express as px
# fig = px.choropleth(df, geojson=busstops, locations='BusStop number', color='number of bus'
#                           )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()
### Using dash dependicies to do instead urhhhhh####

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import plotly.express as px
# import webbrowser
# from threading import Timer

# app = dash.Dash(__name__)
# app.layout = html.Div([
#     html.P("Singapore Bus Stops"),
#     dcc.Dropdown(id="Information",
#                  options=[
#                      {"label": "Claims", "value": "Claims"},
#                      {"label": "Premiums", "value": "Premiums"},
#                      {"label": "Sum Assured", "value": "Sum Assured"}],
#                  multi = False,
#                  value="Claims",
#                  style={'width': "40%"}
#                  ),
#     dcc.Graph(id="choropleth"),
# ])
# @app.callback(
#     Output("choropleth", "figure"),
#     Input(component_id='Information', component_property='value'),)
# def display_choropleth(candidate):
#     fig = px.choropleth(
#         df, geojson=busstops, color=candidate,
#         locations="BusStop number", featureidkey="properties.number",
#         projection="mercator", range_color=[0, 6500])
#     fig.update_geos(fitbounds="locations", visible=False)
#     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#     return fig

# def open_browser():
#     webbrowser.open_new('http://127.0.0.1:8050/')

# if __name__ == '__main__':
#     Timer(2,open_browser).start();
#     app.run_server(debug=True)
