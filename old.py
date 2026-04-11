#django pillow python-dotenv psycopg2-binary 

#no 1 create a project 
#django-admin - is an additional program for working with django
#django-admin startproject project_name - creates a separate folder with the project 
#django-admin startproject project_name . -creates a project in the folder we are currently in

#no 2 create an application/app (python manage.py startapp app_name)
#python manage.py startapp application_name (main, users,)

#no 3 - starting a local server
#python manage.py runserver

#syntax of the template engine

#{% name_function %} 

#TODO: navigate to http://127.0.1:8000/about/
#{% url 'link_name' gets the link by name %}
#python manage.py migrate - executes migration files for all applications.
# python manage.py createsuperuser - creates a superuser (admin) for the admin panel 

#no 4 - migrate - to create tables in the database
# python manage.py migrate      # to create tables in the database
# python manage.py makemigrations  # to create migration files (files with instructions for creating tables in the database)
# python manage.py migrate      # to create tables in the database according to the migration files

#no 5
#uuid.uuid4() - generates a random uuid (universally unique identifier) - a unique string of characters that can be used as an identifier for objects in the 
# database. It is often used as a primary key for models in django to ensure that each object has a unique identifier.