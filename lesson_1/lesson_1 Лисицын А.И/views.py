from new_day_framework.templator import render


class Index:
    def __call__(self, request):
        return '200 duper', render('index.html')


class Contact:
    def __call__(self, request):
        return '200 OK', render('contact.html')


class About:
    def __call__(self, request):
        return '200 OK', render('about.html')



