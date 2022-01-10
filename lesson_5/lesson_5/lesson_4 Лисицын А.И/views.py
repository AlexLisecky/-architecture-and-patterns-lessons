from new_day_framework.templator import render
from variables import *
from pattern import creational_patterns
from pattern import structural_patterns

site = creational_patterns.Engine()
logger = creational_patterns.Logger('main')
routes = {}


@structural_patterns.AppRoute(routes=routes, url='/')
class Index:
    """ Класс контроллер - рендер основной страницы """
    @structural_patterns.Debug(name='Index')
    def __call__(self, request):
        logger.log('запущена главная страница')
        return STATUS_OK, render('index.html', objects_list=site.categories)


@structural_patterns.AppRoute(routes=routes, url='/contact/')
class Contact:
    """ Класс контроллер - рендер страницы контакты """

    @structural_patterns.Debug(name='Contact')
    def __call__(self, request):
        logger.log('запущена страница контакты')
        return STATUS_OK, render('contact.html')


@structural_patterns.AppRoute(routes=routes, url='/about/')
class About:
    """ Класс контроллер - рендер страницы О сайте """

    @structural_patterns.Debug(name='About')
    def __call__(self, request):
        logger.log('запущена страница о нас')
        return STATUS_OK, render('about.html')


@structural_patterns.AppRoute(routes=routes, url='/course_list/')
class CoursesList:
    """ Класс контроллер - рендер страницы со списком курсов """

    @structural_patterns.Debug(name='CoursesList')
    def __call__(self, request):
        logger.log('Список курсов')
        try:
            print('ttyt')
            category = site.find_category_by_id(int(request['get_params']['id']))
            print('ttyt')
            return STATUS_OK, render('course_list.html', objects_list=category.courses, name=category.name,
                                     id=category.id)
        except KeyError:
            return STATUS_OK, 'No courses have been added yet'


@structural_patterns.AppRoute(routes=routes, url='/create_course/')
class CreateCourse:
    """ Класс контроллер - рендер страницы c созданием курса """
    category_id = -1

    @structural_patterns.Debug(name='CreateCourse')
    def __call__(self, request):
        logger.log('Создание курса')
        if request['method'] == 'POST':
            logger.log('активирован метод POST')
            data = request['post_params']

            name = data['name']
            name = site.decode_value(name)

            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                course = site.create_course('record', name, category)
                site.courses.append(course)

            return STATUS_OK, render('course_list.html', objects_list=category.courses,
                                     name=category.name, id=category.id)

        else:
            c = request['get_params']
            logger.log(c)
            try:
                logger.log('активирован метод GET')
                self.category_id = int(request['get_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return STATUS_OK, render('create_course.html', name=category.name, id=category.id)
            except KeyError:
                return STATUS_OK, 'No categories have been added yet'


@structural_patterns.AppRoute(routes=routes, url='/create_category/')
class CreateCategory:
    """ Класс контроллер - рендер страницы c созданием категории """

    @structural_patterns.Debug(name='CreateCategory')
    def __call__(self, request):
        logger.log('создание категории')
        logger.log(request)
        if request['method'] == 'POST':
            # метод пост
            logger.log(f'Request POST {request}')
            data = request['post_params']
            logger.log(f'Данные с POST запроса {data}')
            name = data['name']
            name = site.decode_value(name)

            category_id = data.get('category_id')

            logger.log(f'Категория id {category_id}')

            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)
            site.categories.append(new_category)

            return STATUS_OK, render('index.html', objects_list=site.categories)
        else:
            categories = site.categories
            return STATUS_OK, render('create_category.html', categories=categories)


@structural_patterns.AppRoute(routes=routes, url='/category_list/')
class CategoryList:
    """ Класс контроллер - рендер страницы cо списком категорий """

    @structural_patterns.Debug(name='CategoryList')
    def __call__(self, request):
        logger.log('Список категорий')
        return STATUS_OK, render('category_list.html', objects_list=site.categories)


@structural_patterns.AppRoute(routes=routes, url='/copy_course/')
class CopyCourse:
    """ Класс контроллер - рендер страницы c копированием курса """

    @structural_patterns.Debug(name='CopyCourse')
    def __call__(self, request):
        logger.log('копирование курса')
        request_params = request['get_params']
        print(site.decode_value(request_params['name']))
        try:
            name = site.decode_value(request_params['name'])
            print(name)
            old_course = site.get_course(name)
            print(old_course)
            if old_course:
                new_name = f'copy_{name}'
                new_course = old_course.clone()
                new_course.name = new_name
                site.courses.append(new_course)
                print(site.courses)

            return STATUS_OK, render('course_list.html', objects_list=site.courses)
        except KeyError:
            return STATUS_OK, 'No courses have been added yet'


class NotFound404:
    """ Класс контроллер - рендер страницы с ошибкой 404 """

    @structural_patterns.Debug(name='NotFound404')
    def __call__(self, request):
        logger.log('страница не найдена')
        return STATUS_404, '404 PAGE Not Found'
