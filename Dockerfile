FROM python:3.7.3
MAINTAINER Rama
LABEL version="1.3"

COPY . /app
WORKDIR /app
RUN rm -rf migrations
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0" ]