from views import Index, Contact, About


def secret_front(request):
    request['secret'] = 'secret'


def key_front(request):
    request['key'] = 'key'


fronts = [secret_front, key_front]

routes = {
    '/': Index(),
    '/contact/': Contact(),
    '/about/': About(),

}
