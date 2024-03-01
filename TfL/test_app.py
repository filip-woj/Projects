import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=['https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/darkly/bootstrap.min.css'])

# ----------------------------------------------------------------------------------
# Import and clean dataset
df = pd.read_csv('data_with_long_lat.csv')
df.columns = [col.lower() for col in df.columns]



df.rename(columns = {'downo' : 'day num'}, inplace=True)
df.rename(columns = {'daytype' : 'day'}, inplace=True)
df.rename(columns = {'downo' : 'day of week'}, inplace=True)
df.rename(columns = {'jnytyp' : 'jny type'}, inplace=True)


dropdown_style = {
            'width': '50%',  
            'font-size': '16px', 
            'color': '#141718', 
            'border-radius': '4px',
            'border': '2px solid #343a40', 
            'background-color': '#b8c2cd', 
            'padding': '10px',
            'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.1)'}

# ----------------------------------------------------------------------------------
# Get unique station names
xstations = df['startstn'].unique()

# Create a dictionary to map station names to their string representations
station_dict = {str(station): station for station in xstations}

# Create a list of dictionaries for dropdown options
station_dropdown = [{'label': key.strip().title(), 'value': value} for key, value in station_dict.items()]


# ----------------------------------------------------------------------------------
# Pre process data needed inside the callback function

def preprocess_data(df, mode_slctd, station_slctd):
    # Filter data for bar chart
    bar_chart_df = df[(df['subsystem'] == mode_slctd) & (df['startstn'] == station_slctd)]
    
    # Calculate the number of journeys by day for the bar chart
    order_of_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    jny_by_day = bar_chart_df['day'].value_counts()
    jny_by_day_df = jny_by_day.reset_index()
    jny_by_day_df.columns = ['Day', 'Journeys']

    # Calculate the number of journeys from each start station for the scatter plot
    scatterplot_df = df[df['subsystem'] == mode_slctd]
    scatterplot_df['startstn'] = scatterplot_df['startstn'].str.title().str.strip()
    start_station_counts = scatterplot_df['startstn'].value_counts().reset_index()
    start_station_counts.columns = ['startstn', 'num_journeys']

    # Merge with the original dataframe to get longitude and latitude for the scatter plot
    merged_df = pd.merge(start_station_counts, scatterplot_df[['startstn', 'longitude', 'latitude']], on='startstn', how='left')
    merged_df = merged_df.sample(frac = 0.01)

    return jny_by_day_df, merged_df




# ----------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Transport for London - One Week in 2009", style={'text-align': 'center'}),

    dcc.Dropdown(id='select_mode',
                 options=[
                     {"label": 'Bus', "value": "LTB"},
                     {"label": 'Underground', "value": "LUL"},
                     {"label": 'National Rail', "value": "NR"},
                     {"label": 'Docklands Light Railway', "value": "DLR"},
                     {"label": 'Overground', "value": "LRC"},
                     {"label": 'Tram', "value": "TRAM"}],
                 multi=False,
                 value='LUL',  # London Underground will be the initial/defualt value
                 style=dropdown_style
                 ),
    dcc.Dropdown(id='select_station',
                 options=station_dropdown,
                 searchable=False,
                 multi=False,
                 placeholder='Search for a station',
                 style=dropdown_style,
                 value = None
                 ),
    html.Div(id='output_container', children=[]),
    html.Br(),  # break line

    dcc.Graph(id='jny_by_day', figure={}),
    dcc.Graph(id='jny_by_startstn', figure={})
])


# ----------------------------------------------------------------------------------
# Connect graphs with Dash components
@app.callback(
    [Output(component_id = 'output_container', component_property = 'children'), # Output will be children in html.Div.
     Output(component_id = 'jny_by_day', component_property = 'figure'),
     Output(component_id = 'jny_by_startstn', component_property = 'figure')], # Don't use square brackets if only one Output
    [Input(component_id = 'select_mode', component_property = 'value'),
     Input(component_id = 'select_station', component_property = 'value')]
)

def update_graph(mode_slctd, station_slctd): # each argument connects to an input (above). One input = one argument, two inputs = two arguments etc. The argument always refers to the component property
    print(mode_slctd)
    print(type(mode_slctd))
    print(station_slctd)
    print(type(station_slctd))

    container = f"The mode of transport chosen by the user was: {mode_slctd}"

    jny_by_day_df, merged_df = preprocess_data(df, mode_slctd, station_slctd)



    # Build bar chart
    order_of_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    bar_chart = px.bar(jny_by_day_df, x = 'Day', y = 'Journeys',
                       title = 'Number of Journeys Each Day',
                       labels = {'Day' : 'Day', 'Journeys' : 'Journeys'},
                       template = 'plotly_dark',
                       category_orders= {'Day' : order_of_days})


    # Create the scatter plot with longitude, latitude, and number of journeys
    scatter_plot = px.scatter_mapbox(merged_df, lat='latitude', lon='longitude', hover_name='startstn',
                                    hover_data={'startstn' : True, 'num_journeys': ':,.0f', 'longitude' : False, 'latitude' : False}, 
                                    title = 'Number of Journeys Started at Each Station',
                                    size='num_journeys',
                                    labels={'num_journeys': 'Number of Journeys'},
                                    size_max = 15,
                                    color='num_journeys',  # Color of points based on number of journeys
                                    color_continuous_scale=px.colors.sequential.Viridis,
                                    zoom=10,  # Set the initial zoom level
                                    mapbox_style="open-street-map")

    

    return container, bar_chart, scatter_plot # what is returned here goes into the output. If you have two outputs you have to return two things here. The order of the return matters

# ----------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)