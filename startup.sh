#!/bin/sh
source venv/bin/activate
python -m flask run
gunicorn --workers 4 --bind 0.0.0.0:5000 --access-logfile - --error-logfile - wsgi:app