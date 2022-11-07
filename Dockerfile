FROM python:3.9
LABEL maintainer = "Vyacheslav Tyurin <tvm91@yandex.ru>"
# RUN mkdir /app
WORKDIR /
COPY . .
# RUN python -m venv venv
# RUN venv/bin/pip install --upgrade pip
RUN pip install -r requirements.txt
ENV FLASK_ENV="docker"
EXPOSE 5000

CMD ["python", "start.py"]
# CMD . venv/bin/activate && exec python start.py