# Project3_NBA_Analysis

# Overview

This project visualizes historical and current NBA player statistics using free public APIs to analyze how the shift toward 3-point shooting has impacted scoring trends and efficiency metrics. The application features an interactive drop-down menu to select a player and dynamically updates three charts to display their shot profile trends between 2013 and 2023.


# Visualizations
__Line Chart:__ Shows the trend of shot selection over time, with one line for total field goal attempts and another for 3-point attempts.
Scatter Plot: Displays the relationship between 3-point field goal percentage and scoring average by year.

__Stacked Bar Chart:__ Illustrates the distribution of shot types over the ten-year period.


How to Use & Interact with the Project

Setup the Database:
This project requires PostgreSQL for data storage.
Install and configure the database using the SQL scripts provided in the /SQL Scripts folder.
Run the Server Application:
Node.js is required to run the backend API.
Start the server by running the appropriate script (see instructions in the repo).
Access the Application:
Once the server is running, open a browser and go to:
http://localhost:3000
Interact with the Visuals:
Select an NBA player from the drop-down menu.
The charts will automatically update with the player’s data.
Ethical Considerations

This project follows ethical data practices by:
✅ Using publicly available data: The dataset is obtained from a free public API with no data scraping involved.
✅ Ensuring local data storage: The data is stored locally and is not shared externally.
✅ Avoiding data manipulation: The dataset is unaltered and not enriched with external data sources.
Data Sources & References

API GitHub Repo: nba_api GitHub
API Documentation: NBA API Docs
Sample Code References:
Snippets from nba_api GitHub repository
Assisted by ChatGPT for syntax corrections and optimization
Data Structure

The PostgreSQL database contains over 13,000 records, distributed across:
4 Tables
2 Views

 
# Dependencies
__Python:__

__nba_api__: Install and use this library to **fetch NBA player statistics** from a free public API.  

__pandas__: Use this to **structure, clean, and manipulate NBA data** before storing or visualizing it. 

__time__: Implement this module to **add delays between API requests** and prevent rate limits.  

__JavaScript:__

__node.js__: Install and run this to **set up a server that retrieves NBA data** from the database.
 
__D3.js__: Use this library to **create interactive charts that visualize player performance trends**. 

__Express.js__: Implement this lightweight framework to **handle API requests between the front end and database**.
   
__PostgreSQL client for Node.js:__ Use this database client to **connect the Node.js server to PostgreSQL and fetch player stats**.  

Install and use __nba_api__ to fetch player data, __pandas__ to clean and structure it, __time__ to manage API requests, __node.js__ and __Express.js__ to build a server, __pg__ to connect to the database, and __D3.js__ to visualize the data dynamically.


# How to Use

1. Clone the Repository:
git clone https://github.com/YOUR_GITHUB_USERNAME/nba-performance-analytics.git
cd nba-performance-analytics
Set Up PostgreSQL Database:
Install PostgreSQL if not already installed.
Execute the provided SQL scripts to create the necessary tables and views.
Install Required Dependencies:
Install Python libraries:
pip install nba_api pandas
Install Node.js libraries:
npm install express pg d3
Start the Server:
node server.js
Access the Dashboard:
Open http://localhost:3000 in your browser.
Select an NBA player from the drop-down to view performance analytics.
Evaluation Criteria
