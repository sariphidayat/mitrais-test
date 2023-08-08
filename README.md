# mitrais

## install required libraries

```
pip install -r requirements.txt
```

## database setup

Adjust the credential on my.cnf file:

```
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8
protocol = tcp
```

## migrate

```
python manage.py migrate
```

## start the dev server

```
python manage.py runserver
```

## unit test

```
python manage.py test
```
