class RegistryHolder(type):
    count = 0

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        '''
        <class '__main__.Animal'>
        <class '__main__.Bear'>
        <class '__main__.Cat'>
        '''
        cls.count += 1
        return new_cls


class Animal(metaclass=RegistryHolder):

    count = 0

    def __init__(self):
        Animal.count += 1


class Bear(Animal):
    pass


class Cat(Animal):
    pass


animal = Animal()
animal1 = Animal()
animal2 = Animal()
animal3 = Animal()

animal4 = Bear()

animal5 = Cat()

print(Animal.count)

print(RegistryHolder.count)


class Dog(Animal):
    pass


print(RegistryHolder.count)