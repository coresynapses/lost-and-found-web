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
pip install -r .\requirements.txt

```

```
# If you are on macOS/Linux, this code is for you:
mkdir .env
python -m venv .env
source .\.env\Scripts\activate
pip install -r .\requirements.txt
```

To verify that Django works, run the server:

```
python manage.py runserver 8080
```

Visit http://localhost:8080 to check that the website works.

## A Note about `.gitignore`

### DO NOT DELETE THE `.gitignore` FILE!

`.gitignore` blacklists everything by default and only whitelists the
necessary files.

### AVOID MODIFYING THE `.gitignore` FILE!

You should only whitelist a directory or a file if it's critical to
the project. This will prevent a lot of issues with git merges, file
pollution, and incompatible database migrations in the future.

## To Work With This Repo (Both Frontend and Backend)

Before you start working with the code base, you need to 
- start the Python virtual environment, 
- set up the database, and 
- run the server.

### Start the Python Virtual Environment

You do this by executing the following in the project root directory:

```
.\.env\Scripts\Activate.ps1
```

### Setup the database

Before executing this command, delete:
- `db.sqlite3`
- any `migrations` directories that are 

You do this by executing the following in the project root directory:

```
.\scripts\Setup.ps1
```

### Run the server

You do this by executing the following in the project root directory:

```
python manage.py runserver 8080
```

### Load the website

Go to http://localhost:8080.
