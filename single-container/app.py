import dash
from flask import current_app
import dash_html_components as html
import dash_core_components as dcc
from getRole import getRole

#import ssl
#context = ssl.SSLContext()
#context.load_cert_chain('fullchain.pem', 'privkey.pem')

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
    html.H4('Choose the colleague to get query'),
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'Azadeh', 'value': 'ah'},
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
def update_output(value):
    query = getRole(value)
    name = query.get('name')
    role = query.get("role")
    if not name == 0:
      return html.H1([name,' is the ',role])
      #return [name,' is the ',role]


if __name__ == '__main__':
    context = ('cert.pem','key.pem')
    app.run_server(debug=True, host="0.0.0.0", port=1980, ssl_context=context)
    #app.run_server(debug=True, host="0.0.0.0", port=1980)
