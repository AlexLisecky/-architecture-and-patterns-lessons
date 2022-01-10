"""Скрипт запуска debug или fake """

from wsgiref.simple_server import make_server
from new_day_framework.main import DebugApplication, FakeApplication
from urls import fronts
from views import routes


def run():

    answer = input('В каком режиме запустить? D - дебаг режим , F - fake режим: ')
    if answer == 'd'.lower():
        debug = DebugApplication(routes, fronts)
        with make_server('', 8000, debug) as httpd:
            print('Work on port 8000')
            httpd.serve_forever()

    elif answer == 'f'.lower():
        fake = FakeApplication(routes, fronts)
        with make_server('', 8000, fake) as httpd:
            print('Work on port 8000')
            httpd.serve_forever()

run()