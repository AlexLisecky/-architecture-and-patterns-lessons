import quopri
from parse_get_post import GetRequests, PostRequests


class NotFound:
    """
    Рендер шаблона страницы при неподходящем URL
    """

    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class Application:
    """
    Основной класс фрейморка Application
    """

    def __init__(self, routes, fronts):
        """
        Конструктор фреймворка
        :param routes словарь с {URL:VIEW}
        :param fronts список котроллеров обрабатывающих запросы к приложению
        """
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        """
        :param environ: словарь данных от сервера
        :param start_response: функция для ответа серверу
        """
        path = environ['PATH_INFO']
        request_method = environ['REQUEST_METHOD']
        request = {}

        if request_method == 'GET':
            get_params = GetRequests().get_request_params(environ)
            request['get_params'] = get_params

        if request_method == 'POST':
            post_params = PostRequests().post_request_params(environ)
            request['post_params'] = post_params
            self.show_params(post_params)

        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes:
            view = self.routes[path]
        else:
            view = NotFound()

        for front in self.fronts:
            front(request)

        code, body = view(request)
        response_headers = [('Content-type', 'text/html')]

        start_response(code, response_headers)
        return [body.encode('utf-8')]

    def show_params(self, message):
        print(message)

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
