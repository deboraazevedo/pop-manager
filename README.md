# POP Manager

![POP-RN](logo.png)

POP RN management system, RNP's point of presence at Rio Grande do Norte (Brazil).

Create containers with all project's dependencies.
```bash
$ docker-compose build
```
Create database and execute migration.
```bash
$ docker-compose run web python manage.py makemigrations
```
```bash
$ docker-compose run web python manage.py migrate
```

Installation of all Node.js dependencies.
```bash
$ docker-compose run web npm install
```
Installation of all Bower dependencies.
```bash
$ docker-compose run web bower install
```
Run tests.
```bash
$ docker-compose run web ./runtests
```
