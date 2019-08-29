from project_1.server import server  # Importing Flask server
import utility as util               # Contains the data processing functions
import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px



# Start the dash app end point on the Flask server
app = dash.Dash(name='top_crimes', server=server, url_base_pathname='/top_crimes/')

 

# ------------------- Ratio of top 10 crimes for last 4 years starts from here ------------------------

# Import the data for generating pie chart for top 10 crimes for last 4 years

top_crimes_per_year = util.top_crimes_per_year()


# Generate the pie chart for top 10 crimes for last 4 years

fig = make_subplots(
    rows=2,
    cols=2,
    specs=[
        [{'type': 'domain'}, {'type': 'domain'}],  # This line inserts 2 pie charts in one row
        [{'type': 'domain'}, {'type': 'domain'}]   # This line inserts 2 pie charts in second row
    ],
    subplot_titles=['2016', '2017', '2018', '2019']
)


# Add data logic to the pie charts defined above

# For Year 2016
fig.add_trace(
    go.Pie(
        labels=top_crimes_per_year['Primary Type'],
        values=top_crimes_per_year[2016],
        name="Year 2016"
    ),
    1,  # row 1
    1   # column 1
)
 
# For year 2017
fig.add_trace(
    go.Pie(
        labels=top_crimes_per_year['Primary Type'],
        values=top_crimes_per_year[2017],
        name="Year 2017"
    ),
    1,  # Row 1
    2   # Column 2
)
 
# For year 2018
fig.add_trace(
    go.Pie(
        labels=top_crimes_per_year['Primary Type'],
        values=top_crimes_per_year[2018],
        name="Year 2018"
    ),
    2,  # row 2
    1   # column 1
)
 
# For year 2019
fig.add_trace(
    go.Pie(
        labels=top_crimes_per_year['Primary Type'],
        values=top_crimes_per_year[2019],
        name="Year 2019"
    ),
    2,  # row 2
    2   # column 2
)
 
# Add chart title
fig.update_layout(
    title_text="Distribution of top 10 crimes for last 4 years"
)
 
 
# ------------------- Scatter plot of top 10 crimes for all districts starts from here ------------------------
 
 
# Import the data for generating the scatter plot for top 10 crimes in Chicago
crimes_spread_by_district= util.crimes_location()
 
# List to fetch the data for top 10 crimes
top_10_crimes = ["THEFT", "BATTERY", "NARCOTICS", "CRIMINAL DAMAGE", "OTHER OFFENSE", "ASSAULT", "DECEPTIVE PRACTICE", "BURGLARY", "MOTOR VEHICLE THEFT", "ROBBERY"]
 
# Get the records for top 10 crimes from the original data set
crimes_spread_by_district = crimes_spread_by_district.loc[crimes_spread_by_district['Primary Type'].isin(top_10_crimes)]
 
# Get the data for last 4 years
crimes_spread_by_district = crimes_spread_by_district.loc[crimes_spread_by_district['Year'] > 2015]
crimes_spread_by_district = crimes_spread_by_district.astype({'X Coordinate': 'int64', 'Y Coordinate': 'int64'})
 
# Generate the scatter plot
fig2 = px.scatter(
    crimes_spread_by_district, x='X Coordinate', y='Y Coordinate', color='Primary Type'
)
 
# Add the title to the chart
fig2.update_layout(
    title_text="Top 10 Crimes in last 4 years"
)
 
 
# Generate the html friendly container to show all the charts on the end point url
app.layout = html.Div([
    dcc.Graph(
        id='top_crimes_ratio_by_year',
       figure=fig
    ),
 
    dcc.Graph(
        id='top_crimes_recent_years',
        figure=fig2
    )
])
