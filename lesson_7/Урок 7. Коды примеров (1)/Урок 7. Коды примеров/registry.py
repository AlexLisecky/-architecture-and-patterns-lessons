class RegistryHolder(type):
    REGISTRY = {}
    count = 0

    def __new__(cls, name, bases, attrs):
        new_cls = type.__new__(cls, name, bases, attrs)
        cls.REGISTRY[new_cls.__name__] = new_cls
        cls.count += 1
        return new_cls

    @classmethod
    def get_registry(cls):
        return dict(cls.REGISTRY)


class BaseRegisteredClass(metaclass=RegistryHolder):
    pass


print("до создания подклассов: ")
[print(f'\t{k}') for k in RegistryHolder.REGISTRY]


class FirstClass(BaseRegisteredClass):
    def __init__(self, *args, **kwargs):
        pass


class SecondClass(BaseRegisteredClass):
    def __init__(self, *args, **kwargs):
        pass


print("\n после создания подклассов: ")
[print(f'\t{k}') for k in RegistryHolder.REGISTRY]
print(RegistryHolder.count)
