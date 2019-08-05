# Restaurant chooser

Server API that will allow employees to select restaurant for lunch.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
pip3 install djangorestframework
pip3 install drf-extensions
pip3 install django-filter
pip3 install django
pip3 install drf-yasg
pip3 install packaging  # Requirement from drf-yasg
```

### Installing

A step by step series of examples that tell you how to get a development env running


```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8000
```

## Running the tests

```
python manage.py test
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


# Corner Case django test app
Server API that will allow employees to select restaurant to go to.

Employee/staff user creates restaurant and gets token for for restaurant

`POST /api/restaurant/ {"title": "Restaurant title}`

Provide to the restaurant ACCESS_TOKEN from response.
Upload menu from restaurant:

`POST /api/menu/ {"title": "title", "dishes": "actual repertuar"}`

We are assuming that user in the system is actual employee, unless it has restaurant assigned to him.

`GET /api/menu/?date=2019-08-01`

Will provide the menus for that day

Each employee can vote for the menu

`POST /api/menu/:id/votes/ {"action": 0}`

to vote for the menu

`POST /api/menu/:id/votes/ {"action": 1}`

to vote against menu

`GET /api/menu/result/?date=2019-08-01`

Get winning menu for specified day
