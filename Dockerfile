FROM python:3
MAINTAINER Vyacheslav Tyurin 'tvm91@yandex.ru'
RUN apt-get update -y && apt-get install -y build-essential
COPY . /First-app
WORKDIR /First-app
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ['python']
CMD ['app.py']