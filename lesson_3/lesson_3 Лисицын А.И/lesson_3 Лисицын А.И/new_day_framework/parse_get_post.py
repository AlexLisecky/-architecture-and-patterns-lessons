class GetRequests:
    """ Класс отвечающий за получение параметров из GET-запроса """

    @staticmethod
    def parse_input_data(data: str):
        """
            Метод убирающий лишние символы из строк
            :data str
            :return re dict
        """
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                key, value = item.split('=')
                result[key] = value
        return result

    @staticmethod
    def get_request_params(environ):
        """
            Метод: получаем параметры из GET-запроса
            :data str
            :return re dict
        """
        query_string = environ['QUERY_STRING']
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


class PostRequests:
    """ Класс отвечающий за получение параметров из POST-запроса """

    @staticmethod
    def get_wsgi_input_data(env) -> bytes:
        """
        Получение байтов из post-запроса
        :param env environ словарь переменных окружения
        :return data
        """
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        """
        Декодирование байтов в словарь
        :data bytes
        :return dict
        """
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    @staticmethod
    def parse_input_data(data: str):
        """
        Метод убирающий лишние символы из строк
        :data str
        :return re dict
        """
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                key, value = item.split('=')
                result[key] = value
        return result

    def post_request_params(self, environ):
        """
        Метод обьединяющий остальные методы класса,
        получаем параметры из POST запроса
        :param environ
        :return data
        """
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)

        return data
