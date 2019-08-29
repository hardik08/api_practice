from project_1.server import server  # Importing Flask server
import utility as util               # Contains the data processing functions
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px


# Start the dash app end point on the Flask server
app = dash.Dash(name='theft_analysis', server=server, url_base_pathname='/theft_analysis/')


# Import the data for theft analysis
df = util.theft_crime_data()


# -------------- Theft vs Arrests made per year chart starts from here -----------------

# Create a data frame containing the theft and arrest aggregation per year

theft_vs_arrest_per_year = df.groupby('Year').agg({'Primary Type': ['count'], 'Arrest': ['sum']})


# Data frame will be multi index. So converting the dataframe from multi index to single index

theft_vs_arrest_per_year = theft_vs_arrest_per_year.reset_index()
new_cols = [''.join(t) for t in theft_vs_arrest_per_year.columns]
theft_vs_arrest_per_year.columns = new_cols
theft_vs_arrest_per_year.rename(columns = {'Primary Typecount':'Primary Type', 'Arrestsum':'Arrest'}, inplace = True)


# Generating the chart for the theft vs arrest bar chart
fig = go.Figure(data=[
   go.Bar(name='Crime Type', x=theft_vs_arrest_per_year['Year'], y=theft_vs_arrest_per_year['Primary Type']),
   go.Bar(name='Arrest', x=theft_vs_arrest_per_year['Year'], y=theft_vs_arrest_per_year['Arrest'])
])

# Chart will be a grouped bar chart so assigning the mode and the title to the chart
fig.update_layout(
    barmode='group',
    title_text="Theft Crime vs Arrests per Year"
)


# ------------------ Theft trend per hour of the day starts from here --------------------


# Generating the dataframe containing the statistics for generating the chart

crime_by_hour_trend = df['Hour'].value_counts()
crime_by_hour_trend=crime_by_hour_trend.to_frame().reset_index()
crime_by_hour_trend.columns = ['Hour', 'count']

# Generating the bar chart for show casing the theft trend for every hour of the day
fig2 = go.Figure([
    go.Bar(x=crime_by_hour_trend['Hour'], y=crime_by_hour_trend['count'])
])


# Giving the title to the chart
fig2.update_layout(
    title_text="Theft Distribution by Hour of the day"
)
 

# ------------------ Theft trend per month starts from here ----------------------------------


# Generating the dataframe containing the statistics for generating the chart

crime_by_month_trend = df['Month'].value_counts()
crime_by_month_trend=crime_by_month_trend.to_frame().reset_index()
crime_by_month_trend.columns = ['Month', 'count']

# Generating the bar chart for show casing the theft trend for every month
fig3 = go.Figure([
    go.Bar(x=crime_by_month_trend['Month'], y=crime_by_month_trend['count'])
])

# Giving the title to the chart
fig3.update_layout(
    title_text="Theft Distribution by Month"
)


# ------------------ Theft crime distribution for the all the districts ----------------------------------


# Generating the dataframe containing the required columns for generating the chart
theft_distribution_data = df[['X Coordinate', 'Y Coordinate', 'District']]
theft_distribution_data = theft_distribution_data.astype({'X Coordinate': 'int64', 'Y Coordinate': 'int64'})
theft_distribution_by_district = theft_distribution_data.loc[theft_distribution_data['X Coordinate'] != 0]


# Generating the scatter plot chart for show casing the theft crime distribution for all the districts

fig4 = px.scatter(
    theft_distribution_by_district, x='X Coordinate', y='Y Coordinate', color='District'
)


# Giving the title to the chart
fig4.update_layout(
    title_text="Theft distribution by district"
)

 
# Generate the html friendly container to show all the charts on the end point url

app.layout = html.Div([
    dcc.Graph(
        id='theft_vs_arrest',
        figure=fig
    ),
 
    dcc.Graph(
        id='trend_over_hour_of_day',
        figure=fig2
    ),
 
    dcc.Graph(
        id='trend_over_month',
        figure=fig3
    ),
 
    dcc.Graph(
        id='distribution_by_district',
        figure=fig4
    )
])
