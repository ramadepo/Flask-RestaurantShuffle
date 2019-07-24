#!/bin/bash

if [ ! -d migrations ]; then
    python manage.py db init && \
    sleep 10 && \
    python manage.py db migrate && \
    sleep 5 && \
    python manage.py db upgrade
fi

uwsgi uwsgi/restaurantshuffle.ini

while [ true ]; do
    sleep 86400
done