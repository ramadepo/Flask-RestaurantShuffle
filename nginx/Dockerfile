FROM nginx
MAINTAINER Rama
LABEL version="1.5"

RUN rm /etc/nginx/conf.d/default.conf && rm /etc/nginx/nginx.conf
COPY ./nginx.conf /etc/nginx
COPY ./static /etc/nginx/static
COPY ./default.conf /etc/nginx/conf.d