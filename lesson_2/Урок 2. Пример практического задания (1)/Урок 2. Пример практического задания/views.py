from simba_framework.templator import render


class Index:
    def __call__(self, request):
        status = '200 OK'
        return status, render('index.html', data=request.get('data', None))


class About:

    def __call__(self, request):
        status = '200 OK'
        return status, 'about'


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'
