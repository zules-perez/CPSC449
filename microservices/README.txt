CPSC 449-01
Project 2 - Microservices
Zulema Perez
rancid80s@csu.fullerton.edu 

Adhering to the projects requirements, this project is implemented using Flask, FlaskAPI, WSGI library, PugSQL, foreman, HTTPie, and click among other Python libraries.
In this project two back-end microservices were created to build a microblogging service similar to Twitter.
	
Initializing the Database -

In order to create the database and start the service, make sure to extract the contents of the tarball into a single folder to maintain the file structure. Using the terminal go into the root folder of the decompressed file

enter command: FLASK_APP=users flask init

The database will now be created with a few sample data entries and the microservices will be ready to use.

Starting the services -

After creating the database now start the services by using the terminal while in the root folder

enter command: foreman start

and leave the terminal window running for as long as you require the service to be active.

folder content:

cpsc449_project2

	- dbquery
		- users_query.sql
		- timelines_query.sql

	- timelines.py
	- users.py
	- schema.sql
	- api.cfg
	- Procfile
	- .env
	- README.txt
	- cpsc449-01_project2_restapi.pdf

