Weather Monitoring Application
Ebrasu Bianca-Ana
1.	Project Overview
   
The Weather and Pollution Data Monitoring project aims to provide weather information and pollution index data through a user-friendly web application. This project uses Elasticsearch, Java Spring Boot, and RESTful APIs to store, retrieve, and present weather and pollution data. 

2.	Project Components

2.1	ElasticSearch
1. Elasticsearch
Elasticsearch is will be the database used for data storage, search, and analysis.
2.2	Java Spring Boot
The Spring Boot framework is used to build the back-end of the project. It simplifies the development of robust, scalable, and RESTful web services.
2.3	RESTful API
A RESTful API is developed to interact with the MySQL database. It exposes endpoints for data ingestion, retrieval, and analysis.
2.4	User Interface
A user-friendly web interface is designed to allow the user to access and visualize weather and pollution data. Users can view weather conditions, forecasts, and pollution index information for any selected place and location, as well as see history or predictions for the following days. 

3.	Project Workflow
   
Data Collection: Weather and pollution data are collected from external sources. These sources provide real-time and forecasted information.
Data Ingestion: The collected data is ingested into the MySQL database using the RESTful API endpoints.
API Development: The Spring Boot application provides RESTful endpoints for data ingestion and retrieval. It processes incoming requests, interacts with the database, and responds with data or updates.
User Interface: Users access the web interface to retrieve and visualize data. They can view weather conditions, forecasts, and pollution index information based on their location.

TEHNOLOGIES 

1. Elasticsearch
Elasticsearch is the  database used for data storage, search, and analysis.

Java Spring Boot:
Spring Boot has been selected for the development of the backend due to its ease of creating scalable RESTful web services. This choice provides a robust and user-friendly framework for managing the logic of the application. Spring Boot simplifies the development process, making it easier to build, deploy, and scale applications. The framework's features, such as auto-configuration and a wide range of built-in modules, contribute to the efficiency and scalability of the backend.

RESTful API:
The REST architecture approach has been adopted for the development of APIs due to its simplicity, scalability, and ease of understanding. RESTful APIs are well-suited for communication between different components of the project, providing a standardized and straightforward way to transmit data. This choice aligns with the goal of creating a user-friendly web application, as RESTful APIs are known for their simplicity and ease of integration. The use of RESTful principles contributes to a clear and organized communication structure within the system.

User Interface
The web interface offers advanced search and analysis features, utilizing Elasticsearch.

API DESIGN

Weather and Pollution Data API

1. Get Current Weather and Pollution Data

Endpoint: /api/data/current
Method: GET
Parameters:
location (string): The location for which to retrieve current data.
Response:Current weather and pollution data for the specified location.



2. Get Weather Forecast

Endpoint: /api/data/forecast
Method: GET
Parameters:
location (string): The location for which to retrieve the forecast.
Response: Weather forecast for the specified location.

3. Get Historical Data

Endpoint: /api/data/history
Method: GET
Parameters:
location (string): The location for which to retrieve historical data.
start_date (string): The start date of the historical data (format: YYYY-MM-DD).
end_date (string): The end date of the historical data (format: YYYY-MM-DD).


4. Data Ingestion Endpoints

4.1. Ingest Current Weather and Pollution Data

Endpoint: /api/data/current/ingest
Method: POST

4.2. Ingest Weather Forecast Data

Endpoint: /api/data/forecast/ingest
Method: POST

5. Ingest Weather Forecast Data
Endpoint: /api/data/forecast/ingest

Method: POST


