from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server


def application(environ, start_response):
    setup_testing_defaults(environ)
    method = environ['REQUEST_METHOD']
    print('method', method)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'Hello world from a simple WSGI application!']


with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()

# gunicorn
# pip install gunicorn
# gunicorn get_post:application

# uwsgi
# pip install uwsgi
# uwsgi --http :8000 --wsgi-file get_post.py

# 127.0.0.1:8000?id=1&category=10
