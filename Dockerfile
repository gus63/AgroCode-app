FROM python:3.9
LABEL maintainer = "Vyacheslav Tyurin <tvm91@yandex.ru>"
# RUN mkdir /app
RUN apt-get update -y && apt-get install -y build-essential
COPY . .
WORKDIR /app
# RUN python -m venv venv
# RUN venv/bin/pip install --upgrade pip
RUN pip install -r requirements.txt
# ENV FLASK_DEBUG="docker"
EXPOSE 80
CMD ["python", "start.py"]