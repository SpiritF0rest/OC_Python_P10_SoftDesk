# :hammer_and_wrench: SoftDesk :hammer_and_wrench:

Django Rest Framework API for issue tracking system.

***
## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)

### :newspaper: General Info :newspaper:
***
This is an OpenClassrooms student Django Rest Framework project. 
This application makes it possible to report and follow up on technical problems (Issue Tracking System = ITS).
Contains an authentication system.
- [Postman](https://documenter.getpostman.com/view/18218262/2s946ibr3S): SoftDesk Postman documentation

### :briefcase: Technologies :briefcase:
*** 
- [Django](https://pypi.org/project/Django/4.2.2/): Version 4.2.2
- [Python](https://www.python.org/): Version 3.10.7
- [Pip](https://pypi.org/project/pip/): Version 22.2
- [DjangoRestFramework](https://pypi.org/project/djangorestframework/): Version 3.14.0
- [DRF-simpleJWT](https://pypi.org/project/djangorestframework-simplejwt/): Version 5.2.2

### :wrench: Installation :wrench:
***
In your directory for the project:

Clone repository from:
- [SoftDesk](https://github.com/SpiritF0rest/OC_Python_P10_SoftDesk)

#### :wrench: Virtual environment creation and use :wrench:

```
In terminal from cloned folder :
$ python3 -m venv env

To active the virtual environment:
$ source env/bin/activate

To install modules: 
$ pip install -r requirements.txt

To apply migrations
$ python3 manage.py migrate

To run server:
$ python3 manage.py runserver

To deactive the virtual environment: 
$ deactivate
```

#### :wrench: Migrations :wrench:

```
To apply migrations
$ python3 manage.py migrate

To create a migration after modifying the models
$ python3 manage.py makemigrations
```

:snake: Enjoy :snake:
