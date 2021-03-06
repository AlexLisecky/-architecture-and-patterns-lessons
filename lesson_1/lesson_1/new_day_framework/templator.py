import os
from jinja2 import Template


def render(template_name, folder='templates', **kwargs):
    path = os.path.join(folder, template_name)

    with open(path,encoding='utf-8') as file:
        template = Template(file.read())

    return template.render(**kwargs)
