""" Файл с URL и Front_controllers для проекта """
from views import Index, Contact, About


def secret_front(request):
    request['secret'] = 'secret'


def key_front(request):
    request['key'] = 'key'


def create_message(request, message=''):
    request['message'] = message


fronts = [secret_front, key_front, create_message]

routes = {
    '/': Index(),
    '/contact/': Contact(),
    '/about/': About(),

}
