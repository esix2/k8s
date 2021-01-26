import dash
import socket as s
import dash_html_components as html
import dash_core_components as dcc
from flask import Flask
import requests
from datetime import datetime
from getName import getName
from query import query

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H2(
    html.Table([
        html.Tr([html.Th('This is a simple demo for '),
                 html.Th(html.Img(style={"padding": 0, "width": "160px", "height": "90px"}, src=app.get_asset_url('logo-m3connect.png'))),
                 html.Th('staff query'),
                 ]),
    ])),
    #html.H1(['This is simple demo for ', html.Img(style={"padding": 0, "width": "160px", "height": "90px"}, src=app.get_asset_url('logo-m3connect.png')), ' interview']),
    html.H2('Choose the colleague to get query'),
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'Azadeh', 'value': 'ah'},
            {'label': 'Ehsan', 'value': 'ez'},
            {'label': 'Jennifer', 'value': 'jj'},
            {'label': 'Justin', 'value': 'je'},
            {'label': 'Max', 'value': 'mm'}
        ],
        value=' '
    ),
    html.Div(id='dd-output-container')
])


@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value')])

def update_output(value):
    try:
      ifQuerry = False
      name = getName(value)
      if not value == " ": 
        ifQuerry = True
        q = query()
        role = q.get_query(value)
        q.disconnect()

      now = datetime.now()
      dt_string = now.strftime("%d.%m.%Y %H:%M:%S")

      if ifQuerry:
        if not name == "NA":
            return [
            html.H1(""), html.H1(""), html.H1("")
            , html.H4([name,' is the ',role])
            , html.P(['Query time: ', dt_string])
            ]
        else:
          return [
          html.H1(""), html.H1(""), html.H1("")
          #, html.H4('The person not found')
          , html.H4(html.Span(' The person not found!'),style={"color":"red"})
          , html.P(['Query time: ', dt_string])
          ]
    except:
        return [
        html.H1(""), html.H1(""), html.H1(""),
        html.P(html.Span(' The database is not reachable. Please refresh the page!'),style={"color":"red"})
        ]

if __name__ == '__main__':
    print(s.gethostbyname(s.gethostname()))
    app.run_server(debug=True, host="0.0.0.0", port=1980)
