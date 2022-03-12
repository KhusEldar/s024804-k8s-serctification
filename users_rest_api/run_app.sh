#!/usr/bin/bash

cd app
gunicorn -w 4 --bind 0.0.0.0:$(echo $PORT) wsgi:app
# "gunicorn", "-w", "4", "--bind", "0.0.0.0:$(echo $PORT)", "wsgi:app"
