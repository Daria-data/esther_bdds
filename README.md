### Les données, alimenter une base de données

#### import2.py + docker-compose
##### Key Missions:

* Creation of a relational database using PostgreSQL in a Docker environment

* Definition of relational schemas for client, product, and sales data

* Importation of data in various formats, including CSV and JSON, into the database

* Integration with Docker Compose to orchestrate containers for database and app

* Automated table creation, dropping, and re-creation to ensure clean data imports

  #### import_mongo.py

* Connection to a MongoDB database using the PyMongo library

* Importation of JSON data from local files into MongoDB cluster 

* Iteration through JSON files in the specified directory for bulk data insertion

* Automated creation of collections based on the JSON file names

* Integration for non-relational data storage
