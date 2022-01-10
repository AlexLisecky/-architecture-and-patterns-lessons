"""Скрипт запуска application """

from wsgiref.simple_server import make_server
from new_day_framework.main import Application
from urls import fronts
from views import routes

application = Application(routes, fronts)


with make_server('', 8000, application) as httpd:
    print('Work on port 8000')
    httpd.serve_forever()

