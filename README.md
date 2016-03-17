# POP Manager

![POP-RN](logo.png)

Management system pop-rn, RNP point of presence in the great northern river.

Create containers with all project dependencies.
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

Installation of all dependencies of Node.js.
```bash
$ docker-compose run web npm install
```
Installation of all dependencies bower.
```bash
$ docker-compose run web bower install
```
Run tests.
```bash
$ docker-compose run web ./runtests
```
