#!/bin/bash

if [ ! -d migrations ]; then
    python manage.py db init && python manage.py db migrate && python manage.py db upgrade
fi

uwsgi uwsgi/restaurantshuffle.ini

while [ true ]; do
    sleep 86400
done