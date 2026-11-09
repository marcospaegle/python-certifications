"""5.2.1-5.2.3 - Imports, math, random."""
import math
import math as m
from math import sqrt as square_root
import random

print(math.sqrt(16), m.pi, square_root(9))  # -> 4.0 3.141592653589793 3.0

print(math.ceil(2.1), math.ceil(-2.1))     # -> 3 -2
print(math.floor(2.9), math.floor(-2.1))   # -> 2 -3
print(math.trunc(2.9), math.trunc(-2.9))   # -> 2 -2
print(type(math.ceil(2.1)).__name__, type(math.sqrt(16)).__name__)  # -> int float
for x in (2.7, -2.7, 2.5):
    print(x, math.floor(x), math.ceil(x), math.trunc(x), int(x), round(x))
# -> 2.7 2 3 2 2 3
# -> -2.7 -3 -2 -2 -2 -3
# -> 2.5 2 3 2 2 2

try:
    math.sqrt(-1)
except ValueError as e:
    print(e)                       # -> math domain error

try:
    import not_a_real_module  # noqa: F401
except ModuleNotFoundError as e:
    print(e)                       # -> No module named 'not_a_real_module'

x = random.random()
print(0.0 <= x < 1.0)              # -> True
print(random.choice([10, 20, 30]) in (10, 20, 30))  # -> True
lotto = random.sample(range(1, 50), 6)
print(len(lotto), len(set(lotto)))  # -> 6 6

try:
    random.sample([1, 2, 3], 4)
except ValueError as e:
    print(e)                       # -> Sample larger than population or is negative

try:
    random.choice([])
except IndexError:
    print("IndexError")            # -> IndexError

random.seed(42)
a = (random.random(), random.random(), random.random())
random.seed(42)
b = (random.random(), random.random(), random.random())
print(a == b)                      # -> True
