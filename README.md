# MDOT-REST APP #

A RESTful API server for mobile resources.

## Installation ##

### Prerequisites ###
To run the app, you must have the following installed:
* Docker
* Docker-compose

### Steps to run ###
First, clone the app:

    $ git clone https://github.com/uw-it-aca/mdot-rest.git

Navigate to the develop branch and copy the sample environment variables into your own `.env` file and change variables if desired:

    $ cd mdot-rest
    $ git checkout develop
    $ cp sample.env .env

Then, run the following command to build your docker container:

    $ docker-compose up --build

You should see the server running when viewing http://localhost:8000 (or at the port set in your `.env` file)

## Development ##

### Running the app with Docker ###

To rebuild the docker container from scratch, run: 

    $ docker-compose up --build

Otherwise, just run:

    $ docker-compose up


### Running unit tests inside the Docker container ###
To run the unit tests, simply run the following command from the repository root:

    $ docker-compose run --rm app bin/python manage.py test