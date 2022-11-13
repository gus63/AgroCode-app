FROM python:3.9
LABEL maintainer = "Vyacheslav Tyurin <tvm91@yandex.ru>"
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . .
EXPOSE 5000
CMD exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - start:app