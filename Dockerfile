FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y build-essential \
    git-core \
    python-dev \
    nodejs-legacy \
    npm

RUN npm install -g bower \
    grunt \
    grunt-cli


RUN pip install --upgrade pip

RUN pip install -r requirements.txt
ADD . /code/
