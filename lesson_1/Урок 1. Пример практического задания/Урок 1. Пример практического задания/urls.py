from datetime import date
from views import Index, About


# front controller
def secret_front(request):
    request['data'] = date.today()


def create_message(request):
    request['message'] = ''


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front, create_message]

routes = {
    '/': Index(),
    '/about/': About(),
}
