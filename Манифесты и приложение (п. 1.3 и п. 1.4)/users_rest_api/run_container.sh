#!/usr/bin/bash

export $(grep -v '^#' .env | xargs)

echo PORT $PORT

docker build -t users_rest_api .
docker run -d -p $PORT:$PORT --name users_rest_api --env-file .env --net=host users_rest_api:latest
