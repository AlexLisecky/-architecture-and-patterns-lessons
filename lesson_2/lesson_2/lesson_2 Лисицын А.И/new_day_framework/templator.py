import os
from jinja2 import Template


def render(template_name: str, folder='templates', **kwargs):
    """
    Функция Render служит для отрисовки HTML
    :param template_name Название файла .html
    :param folder Название директории где хранятся шаблоны
    :return Отрисованный шаблон
    """
    path = os.path.join(folder, template_name)

    with open(path, encoding='utf-8') as file:
        template = Template(file.read())

    return template.render(**kwargs)
