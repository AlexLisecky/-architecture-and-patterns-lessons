from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment


def render(template_name: str, folder='templates', **kwargs):
    """
    Функция Render служит для отрисовки HTML
    :param template_name Название файла .html
    :param folder Название директории где хранятся шаблоны
    :return Отрисованный шаблон
    """
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)
