# TAMIU Lost and Found 

This is the code repository for the TAMIU Lost and Found web frontend
and Django-based backend.

## First Time Setup

You need a version of Python >= 3.10.

Once you have it, you need to create a Python virtual environment.

This is required to install and setup Django in your computer.

To do this, execute the following code inside the repository's root
directory:

```
# If you are on Windows, use Powershell for this code:
mkdir .env
python -m venv .env
.\.env\Scripts\Activate.ps1
python install -r .\requirements.txt

```

```
# If you are on macOS/Linux, this code is for you:
mkdir .env
python -m venv .env
source .\.env\Scripts\activate
python install -r .\requirements.txt
```

To verify that Django works, run the server:

```
python manage.py runserver 8080
```

If you have issues related to the database or migrations, run the
following code:

```
python manage.py migrate
```

Visit http://localhost:8080 to check that the website works.

## For Frontend work

Before you start working with the code base, you need to start the
Python virtual environment and run the server.

You do this by executing the following in the project root directory:

```
.\.env\Scripts\Activate.ps1
python manage.py runserver 8080
```

Most of the frontend work will be done in the following folders:
- TamiuLostAndFound/templates - contains HTML files
- TamiuLostAndFound/static - contains CSS and JS files

Since we are using Django, frontend developers should be familiar with
Django templates.

More information is here:
https://docs.djangoproject.com/en/5.1/topics/templates/

## For Backend work

Before you start working with the code base, you need to start the
Python virtual environment.

You do this by executing the following in the project root directory:

```
.\.env\Scripts\Activate.ps1
```

You don't need to run the server as the changes you make will change
the way the server behaves.

Most of the backend work will be done in the Python files found in the
TamiuLostAndFound folder.

Avoid modifying the following files:
- manage.py
- TamiuLostAndFound/settings.py
- db.sqlite3
