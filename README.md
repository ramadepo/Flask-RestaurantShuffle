python version 3.7

pip install flask
pip install uwsgi
pip install pymysql
pip install flask-sqlalchemy
pip install flask-script
pip install flask-migrate
pip install cryptography

## Generate https key and cert to nginx/certs/
```
    openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout nginx.key -out nginx.crt -days 36500
```
---
## Email setting
* turn off additional authentication of sender's email
* turn on low security application access setting

[HackMD](https://hackmd.io/@uo0IthDnRdahLIQFI95x-A/SkrjwFAGr)
