import dash
import dash_html_components as html
import dash_core_components as dcc
from flask import Flask
import requests
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H2(
    html.Table([
        html.Tr([html.Th('This is a simple demo for '),
                 html.Th(html.Img(style={"padding": 0, "width": "160px", "height": "90px"}, src=app.get_asset_url('logo-m3connect.png'))),
                 html.Th('interview'),
                 ]),
    ])),
    #html.H1(['This is simple demo for ', html.Img(style={"padding": 0, "width": "160px", "height": "90px"}, src=app.get_asset_url('logo-m3connect.png')), ' interview']),
    html.H2('Choose the colleague to get query'),
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'Ehsan', 'value': 'ez'},
            {'label': 'Jennifer', 'value': 'jj'},
            {'label': 'Justin', 'value': 'je'}
        ],
        value=' '
    ),
    html.Div(id='dd-output-container')
])


@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
#def dummy_wait_mesage(value):
#      return [
#      html.H1(""), html.H1(""), html.H1(""),
#      html.H3('the query is sent to the database. Please wait!'),
#      update_output(value)
#      ]

def update_output(value):
    DBisDown=True
    while DBisDown:
      try:
        t = requests.get(f"http://0.0.0.0:2000/{value}").text
        idx1 = t.find(':'); idx2 = t.find('"',idx1+1)+1; idx3 = t.find('"',idx2); idx4 = t.find(':',idx3); idx5 = t.find('"',idx4+1)+1; idx6 = t.find('"',idx5);
        #query = getRole(value)
        name = t[idx2:idx3]
        role = t[idx5:idx6]
        if not name == "role":
          return [
          html.H1(""), html.H1(""), html.H1(""),
          html.H6([html.Span(name,style={"color":"black",'font-weight':'bold'}),' is the ',html.Span(role,style={"color":"black",'font-weight':'bold'})])
          ]
      except:
          return [
          html.H1(""), html.H1(""), html.H1(""),
          html.P(html.Span(' The database is not reachable. Please refresh the page!'),style={"color":"red"})
          ]


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=1980)
