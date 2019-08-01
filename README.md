Todo


##Installation
 
 1. Install OS(Ubuntu) Requirements.

 2.Clone Project
    _git clone <repository> todo_
=======
============================================================================================================================



## Installation
 
 1.Install OS(Ubuntu) Requirements.
 
 2.Clone Project
 
     git clone https://github.com/nancykhullar08/todo.git


## Setting Virtual Environment

    pip install virtualenv
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt    

## Setting Up the database

    pip install psycopg2
    sudo su - postgres
    psql -d todo -U postgres
    CREATE USER your-username WITH PASSWORD your-password;
    ALTER USER your-username WITH SUPERUSER;
    CREATE DATABASE db_name;
    ALTER ROLE your-username SET client_encoding TO 'utf8';
    ALTER ROLE your-username SET default_transaction_isolation TO 'read committed';
    ALTER ROLE your-username SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE db_name TO your-username;
    \q
   
## Make migrations

    python manage.py makemigrations

## Run migrations
   
    python manage.py migrate

## Create a superuser

    python manage.py createsuperuser

## Run Server

    python manage.py runserver


