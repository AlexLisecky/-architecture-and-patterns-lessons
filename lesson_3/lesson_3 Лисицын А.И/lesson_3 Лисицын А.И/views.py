from new_day_framework.templator import render
from variables import *


class Index:
    """
    Класс - рендер основной страницы
    """

    def __call__(self, request):
        return STATUS_OK, render('index.html')


class Contact:
    """
    Класс - рендер страницы контакты
     """

    def __call__(self, request):
        return STATUS_OK, render('contact.html')


class About:
    """
    Класс - рендер страницы О сайте
    """

    def __call__(self, request):
        return STATUS_OK, render('about.html')


class NotFound404:
    """
    Класс - рендер страницы с ошибкой 404
    """

    def __call__(self, request):
        return STATUS_404, '404 PAGE Not Found'
