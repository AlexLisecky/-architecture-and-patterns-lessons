from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server


def parse_input_data(data: str):
    result = {}
    if data:
        # делим параметры через &
        params = data.split('&')
        for item in params:
            # делим ключ и значение через =
            k, v = item.split('=')
            result[k] = v
    return result


def get_wsgi_input_data(env) -> bytes:
    # получаем длину тела
    content_length_data = env.get('CONTENT_LENGTH')
    # приводим к int
    content_length = int(content_length_data) if content_length_data else 0
    # считываем данные если они есть
    data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
    print(data)
    return data


def parse_wsgi_input_data(data: bytes) -> dict:
    result = {}
    if data:
        # декодируем данные
        data_str = data.decode(encoding='utf-8')
        print(data_str)
        # собираем их в словарь
        result = parse_input_data(data_str)
    return result


def application(environ, start_response):
    setup_testing_defaults(environ)
    """
    :param environ: словарь данных от сервера
    :param start_response: функция для ответа серверу
    """
    # получаем данные
    data = get_wsgi_input_data(environ)
    # превращаем данные в словарь
    data = parse_wsgi_input_data(data)
    print(data)  # -> {id: 1, category: 10}
    start_response('200 OK', [('Content-Type', 'text/html')])

    return [b'Hello world from a simple WSGI application!']

# gunicorn
# pip install gunicorn
# gunicorn post_data:application

# uwsgi
# pip install uwsgi
# uwsgi --http :8000 --wsgi-file post_data.py

with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
