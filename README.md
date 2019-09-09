Welcome to my API building project using Python and web servicecs frameworks, Flask and Dash.

Objective:

Primary objective is to develop an end to end executable program to analyze the Chicago Crime rate dataset, while learning API development and creating a web service as a whole product.

Technologies used:

Programming Language - Python
Python libraries - Pandas, Numpy, Dash, Flask, Plotly
Tools - Pycharm, Jupyter Notebook
Dataset - Chicago Crime Rate (available from official website)

Key Objectives Achieved: 
1) Learned how to create and host APIs
2) How to work with UI
3) How to create a microservice
4) Polished Python coding skills
5) End-to-end deployment

Key Findings from the dataset:
1) Crimes are decreasing in Chicago
2) Theft, Battery, Nacrcotics are the top 3 crimes committed in Chicago
3) Arrests made for theft are considerably less than the crimes committed.
4) Chancec of theft is much higher in the afternoon between 12-6 pm.
5) There is a slight spike in theft crimes during summer.

Key Endpoints after deployment:
1) /crimes_yearly_trend
2) /top_crimes
3) /theft_analysis

Number of files in a project: (** IT MAY CHANGE OVER TIME **)
1) server.py - To initiate the server
2) utility.py - For data data loading and pre-processing
3) crimes_yearly_trend.py - Contains logic to show yearly trend for all the crimes. (Will be loaded as an index page)
4) top_crimes.py - Contains logic to show top 10 crimes committed in last 4 years.
5) theft_analysis.py - Contains logic for the analysis of the theft related data.
6) app.py - Main file for the execution. Will call all the end points and will start the server once ran.

How to deploy:

1) Data - Data has to be downloaded from the following link:

https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2

(- Click on the Export button on the top right side.
 - Click on csv button.
 It might take a while for the file downloading to start)

2) Download/ Create all the python files listed above and keep all the files in a single directory. (NOTE: csv file all needs to be in the same directory)

3) IMP: Open utility.py file and rename the csv file in the function definition "load_data()".

4) Install all the dependency python packages listed below:
- pandas
- numpy
- plotly
- dash
- flask

( These can be installed using "pip install <package_name>")

5) Once all the dependent packages are installed run/execute "app.py" file. 

The app will be hosted on your localhost on port 5000. 

You will be able to access different end points by appending the Endpoint name in the url of the running server. (i.e. localhost:5000/top_crimes)


Good Luck. :)
