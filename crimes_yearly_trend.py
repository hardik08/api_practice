from project_1.server import server  # Importing Flask Server
import utility as util               # Contains the data processing functions
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# Start the Dash app on the Flask server
app = dash.Dash(name='crimes_yearly_trend', server=server, url_base_pathname='/crimes_yearly_trend/')


# Import the data for the yearly trend
df = util.crimes_yearly_trend()


# Create a Bar chart for the trend using Plotly graph objects
fig = go.Figure([
   go.Bar(x=df["Year"], y=df["count"])
])


# Add the tile to the chart
fig.update_layout(
    title_text="Yearly Trend for crimes committed in Chicago"
)


# Generate the html friendly container to show the chart on the end point url
app.layout = html.Div([
    dcc.Graph(
        id='yearly_trend',
        figure=fig
    )
])