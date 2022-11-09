FROM python:3.9
LABEL maintainer = "Vyacheslav Tyurin <tvm91@yandex.ru>"
RUN mkdir /app
# RUN apt-get update -y && apt-get install -y build-essential
WORKDIR /app
COPY . .
RUN python -m venv venv
# RUN pip install -U --upgrade pip
# RUN venv/bin/pip3 install -r requirements.txt
# ENV FLASK_DEBUG="docker"
EXPOSE 5000
# CMD ["python", "start.py"]
# CMD . venv/bin/activate && exec python start.py