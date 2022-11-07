FROM python:3.9
LABEL maintainer = "Vyacheslav Tyurin <tvm91@yandex.ru>"
# RUN mkdir /app
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
# RUN python -m venv venv
# RUN venv/bin/pip install --upgrade pip
RUN pip install -r requirements.txt
ENV FLASK_DEBUG="docker"
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["start.py"]