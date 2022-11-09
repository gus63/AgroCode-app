FROM python:3.9
LABEL maintainer = "Vyacheslav Tyurin <tvm91@yandex.ru>"
# RUN mkdir /app
# RUN apt-get update -y && apt-get install -y build-essential
COPY . .
WORKDIR /
RUN python -m venv venv
# RUN venv/bin/pip install --upgrade pip
# RUN pip install -U --upgrade pip
# RUN venv/bin/pip install -r requirements.txt
# ENV FLASK_DEBUG="docker"
EXPOSE 5000
# CMD ["python", "start.py"]
# CMD . venv/bin/activate && exec python start.py