# Project 2 - Data Ingestion & Analysis

***Project.py*** is the script to call the remote api exactly every minute, writing the data to a sql database stored in Amazon RDS.

***Data Screenshot*** is a screenshot of the data table (apidata) produced from the project.py script. The screenshot is large, so you might have to scroll to the right to see the "time" column.

***Project 2 Analysis*** is the Data Science part of this project where I figured out which variables are related and how "pi" is calculated from "factor" by using alternating series.


My process for this project was to first figure out the script and how to pull from the api and push its data to a sql table. Then, I created a process that  pulled and pushed the data to the table exactly every minute. After the script was finished, I was able to export the table as csv and create graphs in tableau to discover the relationships and patterns in the data. Finally, I researched different series that approximate pi until I came across the the alternating series that matched our data.
