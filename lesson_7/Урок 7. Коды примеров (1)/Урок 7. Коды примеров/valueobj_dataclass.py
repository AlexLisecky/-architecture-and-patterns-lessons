# дата - класса
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


p = Point(1, 2)
p1 = Point(1, 2)

print(p == p1)
print(p.x)
# p.x = 1
print(p.__dict__)
