FROM python:3.7.3
MAINTAINER Rama
LABEL version="1.7"

EXPOSE 5000
COPY . /app
WORKDIR /app
RUN rm -rf migrations
RUN pip install -r requirements.txt
ENTRYPOINT [ "./init.sh" ]