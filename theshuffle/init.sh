#!/bin/bash

if [ ! -d migrations ]; then
    python manage.py db init && \
    sleep 10 && \
    python manage.py db migrate && \
    sleep 10 && \
    python manage.py db upgrade
fi

uwsgi uwsgi/theshuffle.ini

while [ true ]; do
    sleep 86400
done