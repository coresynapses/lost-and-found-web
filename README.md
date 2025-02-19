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
python manage.py runserver
```

Visit http://localhost:8000 to check that the website works.

## For Frontend work

## For Backend work
