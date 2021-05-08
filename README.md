# Project 2 - Data Ingestion & Analysis

***Project.py*** is the script to call the remote api exactly every minute, writing the data to a sql database stored in Amazon RDS.

***Data Screenshot*** is a screenshot of the data table (apidata) produced from the project.py script. The screenshot is large, so you might have to scroll to the right to see the "time" column.

***Project 2 Analysis*** is the Data Science part of this project where I figured out which variables are related and how "pi" is calculated from "factor" by using alternating series.

  
  My process for this project was to first figure out the script and how to pull from the api and push its data to a sql table. To do this, I had to create a new database in AWS RDS, and then by using phpmyadmin I was able to create a new table and set up its columns. Afterwards, I created a process that pulled and pushed the data to the table exactly every minute by using a package in python called Twisted. After the script was finished, I was able to export the table as csv and create graphs in tableau to discover the relationships and patterns in the data. Finally, I researched different series that approximate pi until I came across the the alternating series that matched our data.

  For the most part this project went smoothly. One problem I ran into was how to pass the 3 api json values into the sql statement in my script, but I came across the %s placeholder which solved this problem. Ensuring my function ran exactly every minute was also tricky, but after discovering the Twisted package in python I was able to avoid any "drift" in the timing of my api retreival.
