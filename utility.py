import pandas as pd


# Load the data from the csv to a data frame 

def load_data():
	
    df=pd.read_csv("crime_rate.csv")
	
    return df


# Function to pre-process the data for the end point - crimes_yearly_endpoint

def crimes_yearly_trend():

    # Load the data using the load_data function

    df = load_data()

 
    # Count the number of crimes per Year

    yearly_count = df['Year'].value_counts(sort=True)


    # Convert the data to data frame

    yearly_count = pd.DataFrame(yearly_count)

    yearly_count = yearly_count.reset_index()
 

    # Add the column heading to the data frame

    yearly_count.columns = ['Year', 'count']

 

    return yearly_count


# Function to generate the data frame containing geographic information about the crimes being committed

def crimes_location():

    # Load the data using the function

    df = load_data()
	
    # Make a data frame for required data

    data = df[['Year', 'Primary Type', 'Latitude', 'Longitude', 'X Coordinate', 'Y Coordinate', 'District']]

    # Remove the null/NaN values from the data frame

    data = data.dropna()

    return data


# Function to generate the dataframe for the top 10 crimes by frequency in Chicago

def top_crimes_per_year():

    # Load the data using the function

    df = load_data()

    # Make a dataframe by getting the count of All crimes by year
    crimes_type = df.groupby(["Year", "Primary Type"]).size().reset_index(name="count")

    # Formatting the dataframe in the correct format
    crime_types_per_year = crimes_type.pivot(index='Primary Type', columns='Year', values='count')

    # Creating proper column names and filling the null values with 0
    crime_types_per_year = crime_types_per_year.reset_index()
    crime_types_per_year = crime_types_per_year.fillna(0)

    # Aggregating the crimes for all the years and storing it in Total column
    crime_types_per_year.loc[:, 'Total'] = crime_types_per_year.sum(axis=1).astype('int64')

    # Soting the dataframe in descending order by Total
    crime_types_per_year = crime_types_per_year.sort_values('Total', ascending=False)

    # Taking only the top 10 crimes
    top_10_crimes = crime_types_per_year[:10]

    return top_10_crimes

 
# Function to generate a dataframe for the theft analysis

def theft_crime_data():

    # Load the data using the function

    df = load_data()

    # Create the dataframe by selecting the required columns from the original dataset
    data = df[['Date', 'Year', 'Primary Type', 'X Coordinate', 'Y Coordinate', 'District', 'Arrest']]

    # Select the crimes with 'Theft'.
    theft_data = data.loc[data['Primary Type'] == 'THEFT']

    # Create a new column NEW DATE for correcting the format of the date present in the dataframe
    theft_data['New Date'] = pd.to_datetime(theft_data['Date'])

    # Create additional columns for finding the seasonality in the theft related crimes
    theft_data['Month'] = theft_data['New Date'].dt.month
    theft_data['Hour'] = theft_data['New Date'].dt.hour
    theft_data['Week Day'] = theft_data['New Date'].dt.dayofweek

    # Remove the null values
    theft_data = theft_data.dropna()


    return theft_data