import copy


class Original:
    pass


original = Original()
prototype = copy.deepcopy(original)
print(prototype)

prototype.name = 2
print(prototype.name)