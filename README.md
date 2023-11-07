Weather Monitoring Application
Ebrasu Bianca-Ana
1.	Project Overview
The Weather and Pollution Data Monitoring project aims to provide weather information and pollution index data through a user-friendly web application. This project uses MySQL, Java Spring Boot, and RESTful APIs to store, retrieve, and present weather and pollution data. 

2.	Project Components
2.1	MySQL Database
A MySQL database is employed to store both weather and pollution data efficiently. It offers a structured and scalable approach to manage large volumes of data.
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

