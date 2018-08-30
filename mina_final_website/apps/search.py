import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
import pymysql
import textwrap
import configparser
import pandas as pd
from apps.utills import get_userSelectedDays, Database

from app import app

config = configparser.ConfigParser()
config.read('/home/ubuntu/portfolio/mina_final_website/apps/config.ini')
config.sections()
APIlogin = config["token"]

layout = html.Div([

    html.Div([

        html.H1("Do you Wanna Travel somewhere?", style={'font-family': 'Courier New', 'color': 'blue', 'font-weight': 'bold'}),
        html.Br(),
        html.Label('Expecting Travel Days'),
        dcc.Dropdown(
            id=  'travelDays',
            options=[
                {'label': '1', 'value': '1'},
                {'label': '2', 'value': '2'},
                {'label': '3', 'value': '3'},
                {'label': '4', 'value': '4'},
                {'label': '5', 'value': '5'},
                {'label': '6', 'value': '6'},
                {'label': '7+', 'value': '7'},
            ],
            value=int(),
            placeholder = "Select your travel days"

        ),
        html.Br(),
        html.Label('Category(Up To 3)'),
        dcc.Dropdown(
            id='userSelectedCategories',
            options=[
                {'label': 'sightseeing', 'value': 'sightseeing'},
                {'label': 'relaxing', 'value': 'relaxing'},
                {'label': 'eating', 'value': 'eating'},
                {'label': 'shopping', 'value': 'shopping'},
                {'label': 'outdoor', 'value': 'outdoor'}

            ],
            value=[],
            multi=True,
            placeholder="Select Categories of your Travel"
        ),
        html.Div(id="message_alert"),
        html.Br(),
        html.Label('Departure Date'),
        dcc.DatePickerRange(
            id='my-date-picker-range',
            min_date_allowed=dt(2018, 6, 5),
            max_date_allowed=dt(2020, 9, 19),
            start_date=dt.now(),
            end_date_placeholder_text='Optional'
        ),

        html.P(""),
        html.Button(id='submit_button', n_clicks=0, children='Submit', style={"width" : "100%", "margin-top" : "10px"}),
    ]),


    html.Div(id='user_input'),




])

@app.callback(
    dash.dependencies.Output('message_alert', 'children'),
    [dash.dependencies.Input('submit_button', 'n_clicks')],
    [dash.dependencies.State('userSelectedCategories', 'value')]
    )
def update_output(clicks, userSelectedCategories):
    if len(userSelectedCategories) > 3 or len(userSelectedCategories) < 0:
        return html.Label('Please select categories up to 3')

@app.callback(
    dash.dependencies.Output('user_input', 'children'),
    [dash.dependencies.Input('submit_button', 'n_clicks')],
    [dash.dependencies.State('travelDays', 'value'),
     dash.dependencies.State('userSelectedCategories', 'value'),
     dash.dependencies.State('my-date-picker-range', 'start_date'),
     dash.dependencies.State('my-date-picker-range', 'end_date')])

def update_output(clicks, travelDays, userSelectedCategories, start_date, end_date):

    userSelectedDays = get_userSelectedDays(travelDays)

    if len(userSelectedCategories) < 1:
        return None

    db = Database()

    df = pd.DataFrame()
    result_data = db.pullData(userSelectedDays,userSelectedCategories)
    df = pd.DataFrame(result_data)
    df = df.head(6)


    def insertbr(txt):
        str = ""
        for chunk in textwrap.wrap(txt, 45, break_long_words=False):
            str = str + "<br>" + chunk

        return str


    df['description'] = df['description'].apply(lambda x: insertbr(x))


    return  dcc.Graph(id='map', figure={
            'data': [{
                'scope': 'USA-states',
                'type': 'scattermapbox',
                'len': 100,
                'hoverinfo': 'text',
                'hoverlabel': {
                    'bgcolor': "white",
                    'bordercolor': "grey",
                    'font': {
                        'family': "Arial",
                        'size': 15,
                        'color': 'black'
                    }
                },
                'hovertext':df['city_name']+'<br>'+df['description'],
                'lat': df['LAT'],
                'lon': df['LON'],
                'marker': {
                    'color': df['description'],
                    'size': 30,
                    'opacity': 0.3,
                }
            }],
            'layout': {
                'mapbox': {
                    'accesstoken': APIlogin["key"],
                    'center' : {
                        "lat" : 40,
                        "lon" :-100 },
                    'zoom' : 3
                },
                'title': 'Here is your TOP destinations',
                'margin': {'l': 50, 'r': 50, 'b': 50, 't': 50}
            }
        })






app.css.append_css({
    'external_url': APIlogin["url"]
})







if __name__ == '__main__':
    app.run_server(debug=True)