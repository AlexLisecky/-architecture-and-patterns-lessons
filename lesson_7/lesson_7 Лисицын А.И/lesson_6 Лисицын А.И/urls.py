""" Файл с URL и Front_controllers для проекта """
# from views import Index, Contact, About, CoursesList, \
#     CreateCourse, CreateCategory, CategoryList, CopyCourse


def secret_front(request):
    request['secret'] = 'secret'


def key_front(request):
    request['key'] = 'key'


def create_message(request, message=''):
    request['message'] = message


fronts = [secret_front, key_front, create_message]

# routes = {
#     '/': Index(),
#     '/contact/': Contact(),
#     '/about/': About(),
#     '/course_list/': CoursesList(),
#     '/create_course/': CreateCourse(),
#     '/category_list/': CategoryList(),
#     '/copy_course/': CopyCourse(),
#     '/create_category/': CreateCategory(),
# }
