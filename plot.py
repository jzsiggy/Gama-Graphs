import json
import plotly.graph_objects as go
from config import mpb

mapbox_access_token = mpb

with open('data/data.json', 'r') as fp:
  data = json.load(fp)

limits = [(0,100),(100,1000),(1000,10000),(10000,50000)]
colors = ["royalblue","crimson","lightseagreen","orange"]
scale = 5000

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    
    loc = []
    lat = []
    lon = []
    num = []

    for reg in data:
      if data[reg]['entregues'] >= limits[i][0] and data[reg]['entregues'] < limits[i][1]:
        lat.append(data[reg]['latitude'])
        lon.append(data[reg]['longitude'])
        num.append(data[reg]['entregues'])
        loc.append(reg)

        scale = [nb / 1.5 for nb in num]

        text = ['{0} - {1}'.format(city, quant) for city, quant in zip(loc, num)]

    fig.add_trace(go.Scattermapbox(
        lon = lon,
        lat = lat,
        marker = go.scattermapbox.Marker(
            size = scale,
            color = colors[i],
            sizemode = 'area',
        ),
        hoverinfo = 'text',
        text = text,
        name = '{0} - {1}'.format(limits[i][0],limits[i][1]))),


fig.update_layout(
        title_text = 'Face Shields Entregues Pelo Projeto GAMA',
        showlegend = True,
        mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        style='outdoors',
        center=go.layout.mapbox.Center(
            lat=-23,
            lon=-45
        ),
        pitch=0,
        zoom=6
    )
    )

# fig.show()
fig.write_html('html/SE.html', auto_open=True)