"""4.1.3 / 4.1.4 - Parameters, arguments, defaults, *args, **kwargs."""


def describe(name, age, city):
    return f"{name}, {age}, {city}"


print(describe("Ada", 36, "London"))  # -> Ada, 36, London
print(describe(age=36, city="London", name="Ada"))  # -> Ada, 36, London
print(describe("Ada", city="London", age=36))  # -> Ada, 36, London

# `lambda: ...` wraps each bad call in a tiny function so it runs inside try.
for call in (lambda: describe("Ada"),
             lambda: describe(1, 2, 3, 4),
             lambda: describe("Ada", name="Bob", age=1, city="x")):
    try:
        call()
    except TypeError as e:
        print(e)
# -> describe() missing 2 required positional arguments: 'age' and 'city'
# -> describe() takes 3 positional arguments but 4 were given
# -> describe() got multiple values for argument 'name'


def power(base, exp=2):
    return base ** exp


print(power(3), power(3, 3), power(exp=0, base=5))  # -> 9 27 1


def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket


print(add_item(1))                 # -> [1]
print(add_item(2))                 # -> [1, 2]


def modify(lst):
    lst.append(4)


def rebind(lst):
    lst = [0]


data = [1, 2, 3]
modify(data)
rebind(data)
print(data)                        # -> [1, 2, 3, 4]


def total(*args):
    return type(args).__name__, args, sum(args)


print(total())                     # -> ('tuple', (), 0)
print(total(1, 2, 3))              # -> ('tuple', (1, 2, 3), 6)


def show(**kwargs):
    return kwargs


print(show(a=1, b=2), show())      # -> {'a': 1, 'b': 2} {}


def f(a, b=2, *args, c, d=4, **kwargs):
    print(a, b, args, c, d, kwargs)


f(1, c=3)                          # -> 1 2 () 3 4 {}
f(1, 5, 6, 7, c=3, e=9)            # -> 1 5 (6, 7) 3 4 {'e': 9}
try:
    f(1)
except TypeError as e:
    print(e)                       # -> f() missing 1 required keyword-only argument: 'c'


def add3(a, b, c):
    return a + b + c


nums = [1, 2, 3]
print(add3(*nums), add3(**{"a": 1, "b": 2, "c": 3}))  # -> 6 6
print(*nums, sep=",")              # -> 1,2,3
