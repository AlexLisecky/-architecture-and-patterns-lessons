from inspect import getfullargspec


class CannotBeChangeException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__('You cannot change values, create a new one')


class ValueObject:
    # дедает x и y атрибутами экземпляра класса
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        args_spec = ArgsSpec(self.__init__)
        print(args_spec.args[1:])

        def assign_instance_arguments():
            # print(dict(list(zip(args_spec.args[1:], args)) + list(kwargs.items())))
            # и собираем словарь из аргументов
            self.__dict__.update(
                dict(list(zip(args_spec.args[1:], args)) + list(kwargs.items()))
            )

        assign_instance_arguments()

        print('created')
        return self

    def __setattr__(self, name, value):
        raise CannotBeChangeException

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return self.__dict__ != other.__dict__

    @property
    def hash(self):
        return hash(self.__class__) and hash(frozenset(self.__dict__.items()))


class ArgsSpec(object):
    def __init__(self, method):
        # print('getfullargspec', getfullargspec(method))
        # print('getfullargspec 0', getfullargspec(method)[0])
        self._args = getfullargspec(method)[0]

    @property
    def args(self):
        return self._args


class Point(ValueObject):
    # class Point:
    def __init__(self, x, y):
        pass


print('__new__')
point_1 = Point(1, 2)
point_2 = Point(y=2, x=1)

point_1.y = 100

#print(point_1.x)
#print(point_1.y)

#print(point_1 == point_2)
#print(point_1 != point_2)
#print(point_1 is point_2)
