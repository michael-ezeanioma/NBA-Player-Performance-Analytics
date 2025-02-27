# Project3_NBA_Analysis

# Overview

This project visualizes historical and current NBA player statistics using free public APIs to analyze how the shift toward 3-point shooting has impacted scoring trends and efficiency metrics. The application features an interactive drop-down menu to select a player and dynamically updates three charts to display their shot profile trends between 2013 and 2023.


# Visualizations
__Line Chart:__ Shows the trend of shot selection over time, with one line for total field goal attempts and another for 3-point attempts.
Scatter Plot: Displays the relationship between 3-point field goal percentage and scoring average by year.

__Stacked Bar Chart:__ Illustrates the distribution of shot types over the ten-year period.
 
# Dependencies
__Python__

__nba_api__: Install and use this library to fetch NBA player statistics from a free public API.  

__pandas__: Use this to structure, clean, and manipulate NBA data before storing or visualizing it. 

__time__: Implement this module to add delays between API requests and prevent rate limits.  


__JavaScript__

__node.js__: Install and run this to set up a server that retrieves NBA data from the database.
 
__D3.js__: Use this library to create interactive charts that visualize player performance trends. 

__Express.js__: Implement this lightweight framework to handle API requests between the front end and database.
   
__PostgreSQL client for Node.js:__ Use this database client to connect the Node.js server to PostgreSQL and fetch player stats.  

Install and use nba_api to fetch player data, pandas to clean and structure it, python time module to manage API requests, node.js and Express.js to build a server, postgres to connect to the database, and D3.js to visualize the data dynamically.


# How to Use

### How to Use & Interact with the Project

1. Clone the Repository:
git clone https://github.com/YOUR_GITHUB_USERNAME/nba-performance-analytics.git
cd nba-performance-analytics

1. **Set Up the Database**  
   - This project requires PostgreSQL for data storage.  
   - Install and configure the database using the SQL scripts provided in the `/SQL Scripts` folder.  

2. **Run the Server Application**  
   - Node.js is required to run the backend API.  
   - Start the server by running the appropriate script (refer to the instructions in the repository).  

3. **Access the Application**  
   - Once the server is running, open a web browser and go to:  
     **http://localhost:3000**  

4. **Interact with the Visuals**  
   - Select an NBA player from the drop-down menu.  
   - The charts will automatically update with the selected player’s data.  

5. **Ethical Considerations**  
   - The project uses publicly available data from an API, ensuring no unethical data scraping.  
   - Data is stored locally and is not shared externally.  
   - The data remains unaltered and is not enriched with other sources.  



__Data Sources & References:__

API GitHub Repo: nba_api GitHub

API Documentation: NBA API Docs

<!--Project 3 NBA Analysis-->
