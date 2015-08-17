When you begin a TEDx Conference organization, TED usually gives you a licence which restrict the number of attendees to 100 persons until you meet certain criterias.

To select who assist to the conference many TEDxs allow people to subscribe to a list and then the 100 are chosen by random.

# Requirements #

This program was developed on a Asus PC with Linux (Ubuntu 12.04) with Python 2.7 and Django. If you match these, it will be easier to install and run. Otherwise you might need to read some Python and Django documentation to get it working.

# Setup #

  1. On a Linux console create a new virtual environment for Python running next commands:
```
$ wget http://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.7.tar.gz
$ tar xvfz virtualenv-1.7.tar.gz
$ python2.7 virtualenv-1.7/virtualenv.py .
$ source bin/activate
```

> 2. Install Django
```
$ pip install Django
```

> 3. Download tedx-sorteo
```
$ svn checkout http://tedx-sorteo.googlecode.com/svn/trunk/ .
```

> 4. Edit paths: Edit tedxcordoba/settings.py and replace STATIC\_ROOT and TEMPLATE\_DIRS variables in order to make them point to the place where you downloaded the program. For example, if you downloaded the software at '/srv/tedx-sorteo' the values should be:
```
STATIC_ROOT = '/srv/tedx-sorteo/sorteo/static'
TEMPLATE_DIRS = '/srv/tedx-sorteo/sorteo/templates'

```

> 5. Run it
```
$ python manage.py runserver
```

> 6. Test it on a browser opening http://localhost:8000

> 7. Enjoy

# Customization and others #

### Custom Logo ###
If the program is running successfully you might want to customize the logo, to do this just replace the images at sorteo/static.

### Admin console ###
Since this program is made with Django, you can use an admin console to load new data among other simple tasks. Just go to http://localhost:8000/admin user: admin, password: admin.

### Custom Data ###
In order to make easier test the program you downloaded an already populated database, you will need to add your own data. The simplest way to do that is to keep using sqlite3 and replace sorteo\_sorteo table's data:

```
$ sqlite3 tedxcordoba.db
sqlite> select sql from sqlite_master where tbl_name = 'sorteo_sorteo' AND type = 'table';
CREATE TABLE "sorteo_sorteo" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(200) NOT NULL,
    "digits" varchar(3) NOT NULL
)
```

This means that sorteo has an integer for the id then a char/string for the person name and another string for the person id. So, if you have a csv file like 'demo-data.csv' you can delete current data and import the new one following:

```
sqlite> drop table main.sorteo_sorteo;
sqlite> create table main.sorteo_sorteo ("id" integer NOT NULL PRIMARY KEY, 
"name" varchar(200) NOT NULL, "digits" varchar(3) NOT NULL);
sqlite> .separator ";"
sqlite> .import my_own_data.csv sorteo_sorteo

```

# Doubts, feedback, improvements and final words #

This program is working great on my machine, so it should do the same on yours, if it doesn't you may start switching to Linux :D. Anyway there are tons of improvements to be done, so if you have made them and you want to share contribute with the humankind, don't hesitate to ask me commit access.

Also if you have any comment or question, you can reach me at geek PEACE tedxcordoba.com.ar - replace PEACE by @.

Please don't use this software for warlike purposes.