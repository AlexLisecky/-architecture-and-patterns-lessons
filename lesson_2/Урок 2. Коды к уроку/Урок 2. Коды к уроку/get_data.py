from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server


def parse_input_data(data):
    result = {}
    if data:

        params = data.split('&')
        for item in params:

            key, value = item.split('=')
            result[key] = value
    return result


def application(environ, start_response):
    setup_testing_defaults(environ)
    # # 127.0.0.1:8000?id=1&category=10
    query_string = environ['QUERY_STRING']
    print(query_string)  # -> 'id=1&category=10'

    request_params = parse_input_data(query_string)
    print(request_params)  # -> {'id': '1', 'category': '10'}
    start_response('200 OK', [('Content-Type', 'text/html')])

    return [b'Hello world from a simple WSGI application!']


with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()

# gunicorn
# pip install gunicorn
# gunicorn get_data:application

# uwsgi
# pip install uwsgi
# uwsgi --http :8000 --wsgi-file get_data.py

# 127.0.0.1:8000?id=1&category=10
