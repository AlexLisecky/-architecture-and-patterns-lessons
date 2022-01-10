"""Скрипт запуска application """

from wsgiref.simple_server import make_server
from new_day_framework.main import Application,DebugApplication
from urls import fronts
from views import routes

application = Application(routes, fronts)
debug = DebugApplication(routes,fronts)

# with make_server('', 8000, application) as httpd:
#     print('Work on port 8000')
#     httpd.serve_forever()

with make_server('', 8000, debug) as httpd:
    print('Work on port 8000')
    httpd.serve_forever()
