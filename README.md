# Built Integrations Skills Assessment

## Hello!

You've found the skills assessment for the Integrations team at [Built Technologies](https://getbuilt.com/)!
This project represents a contrived version of work similar to what we do each day.
The intent is to get a sense for how you might do if you were doing this work as a part of this team.
There is no expectation that you complete this exercise.
You are free to Google as much as you like or need to.

If you're working on this as a take-home assignment, rather than as a live code pairing, then please constrain yourself to 2hrs, maximum.
Once you've completed the assignment (or time is up, whichever comes first), we'll get back together to review the written code, talk about what you struggled with, and talk about possibilities for how you might improve or change the project in the future.


## Project Info

For this project, we're going to act as a middle-man between the open data [Star Wars API](https://swapi.dev/), and some unknown consumer on the other side. That means we're going to be retrieving data from the open API and then exposing some new endpoints for other clients to pull from. Ideally we'd be passing this data along to another system directly, but right now simplicity is the goal.

The project has been scaffolded for you, and most major components should have an example already in the repo somewhere. The code that's written is not intended to be complete, and it's entirely expected that you will need to use the Django documentation, Google, Stack Overflow, etc. You are also welcome and encouraged to ask us for help if you need it or want to bounce an idea off of us. That's what we're here for and what we want.

Most of this application should follow a fairly standard Django application structure/pattern, but here are some things that might be worth noting:

* We're using function-based views for this project.
* Please don't pull in any API helpers or packages like Django REST Framework.
* We're not really concerning ourselves with front-end code right now.
* All of our endpoints should return JSON.
* This project already has git initialized.
    * Use good commit messages where possible, and commit often as you work.

* Please write a couple of tests along the way.
    * We're not looking for 100% coverage, just want to get the sense that you understand testing.

* Some locations to note within the repo:

    * `integration_code_pairing_root/integration_code_pairing/planets`: This is an example Django app that currently retrieves planet info info (by ID) from the Star Wars API. It stores the info into a local DB so it doesn't have to hit the API for each request.
    * `integration_code_pairing_root/swapi`: This is an API client for the Star Wars API. If you're making a new request to the SW API, please add that here, rather than directly into the Django view/model/etc.

OK, let's get the project setup, and then we can talk about the tasks and features we want to add.

## Project Requirements

* Python 3.7+
* SQLite
* git


## Project Setup 

1. Clone the repository: `git clone https://github.com/epochblue/integrations-skills-assessment.git`
2. `cd` into the project directory: `cd integrations-skills-assessment`
3. Create and activate a virtual environment: `python3 -m virtualenv venv; source venv/bin/activate`
4. Install project requirements: `pip3 install -r requirements.txt`
5. `cd` into the project root directory: `cd integration_code_pairing_root`
6. Run migrations: `python3 manage.py migrate`
7. Run the server: `python3 manage.py runserver`
8. Point browser to `127.0.0.1:8000`


## Tasks

If everything is setup and running, let's pick a task from this list and get started on it!

_Note_: Again, it's not expected, or even necessarily desired, that you finish everything on this list. Pick a couple of that look interesting, and tackle those. We can always talk about the rest.

1. Add a search endpoint to `planets` to allow a consumer to pull the list of planets that have a population over a certain number. Only consider the data we have stored in the local database for this endpoint.
2. The units in the `planet` model are not in Imperial units. As part of our API, we want to return units like inches or miles, rather than centimeters or kilometers. Update the existing endpoints to return those units instead. 
3. The SW API contains a few other resources beyond planets. Add support for the [People resource](https://swapi.dev/documentation#people), and maybe an endpoint or two to retrieve specific records or filter records.
4. Since people and planets can be related to each other (and are in the SW API), implement that relationship within the Django models, views, etc.
