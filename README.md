# SGR Compliance Interview Project

# Short description
Develop a web service so that the users can insert some text and receive a sentiment analysis in real time, using Django (or Flask) for the backend, a
database to store the data and a basic ML model for the sentiment analysis. The project should be containerized using Docker and controlled by Git.

# Project structure
For the frontend it has been used a very simple Angular application displaying a single page with an input form styled with the Material library. 
For the backend it has been chosen Flask with the library psycopg2, a popular PostgreSQL database adapter for Python.
The sentiment analysis is performed using NLTK (Natural Language Toolkit), a leading platform for building Python programs to work with human language data. 

# How to run the application
From the project directory, execute the following command:

<code>docker-compose up --build</code>

Then, you will be able to navigate to http://localhost to see the running application, waiting for your inputs.
