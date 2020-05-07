import json
import plotly.graph_objects as go

mapbox_access_token = 'You_Access_Token'

with open('data/data.json', 'r') as fp:
  data = json.load(fp)

limits = [(0,100),(100,1000),(1000,10000),(10000,50000)]
colors = ["royalblue","crimson","lightseagreen","orange"]
scale = 5000

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    
    lat = []
    lon = []
    num = []

    for reg in data:
      if data[reg]['entregues'] > limits[i][0] and data[reg]['entregues'] < limits[i][1]:
        lat.append(data[reg]['latitude'])
        lon.append(data[reg]['longitude'])
        num.append(data[reg]['entregues'] / 3)

    fig.add_trace(go.Scattermapbox(
        lon = lon,
        lat = lat,
        marker = go.scattermapbox.Marker(
            size = num,
            color = colors[i],
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(limits[i][0],limits[i][1])))


fig.update_layout(
        title_text = 'Face Shields Entregues Pelo Projeto GAMA',
        showlegend = True,
        mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=-23,
            lon=-45
        ),
        pitch=0,
        zoom=5
    )
    )

fig.show()