Environment Setup
==================
1. Install Python version 2.7.5
2. Install Django 1.6.4
3. Install PyYAML for configuration
4. Install oauth2
5. Install MySQL-python

Configuration
=================
* Modify config-template.yaml file with your settings and save it as config.yaml
* Modify the DATABASES variable in settings.py with your database information
* Run python manage.py syncdb to create the tables

Yelp
-----------------
1. Sign up for Yelp API key at http://www.yelp.com/developers/getting_started/api_access
2. Add your Yelp API Access Keys to config.yaml