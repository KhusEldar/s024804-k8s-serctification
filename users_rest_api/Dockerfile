FROM python:3.9
LABEL maintaner "Nikolay Chechulin <nchechulin@aol.com>"

# Env variables to be provided by the `start.sh` script
ARG PORT
ARG DB_HOST
ARG DB_PORT
ARG DB_USER
ARG DB_PASSWORD
ARG DB_NAME

RUN echo $PORT

RUN mkdir -p /var/www/users_rest_api
WORKDIR /var/www/users_rest_api
#COPY app /var/www/users_rest_api/app
#COPY wsgi.py /var/www/users_rest_api
COPY requirements.txt /tmp
COPY . /var/www/users_rest_api/

RUN ls

RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install psycopg2
RUN pip install gunicorn

EXPOSE $PORT

#CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:$(echo $PORT)", "wsgi:app"
CMD ["bash", "run_app.sh"]
# CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi:app"]
