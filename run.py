#!flask/bin/python
#coding:utf-8
from app import app
from werkzeug.contrib.fixers import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    app.run()
