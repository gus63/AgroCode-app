FROM python:3.6
LABEL maintainer = "Vyacheslav Tyurin <tvm91@yandex.ru>"
RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip freeze > requirements.txt
ENV FLASK_ENV="docker"
EXPOSE 5000