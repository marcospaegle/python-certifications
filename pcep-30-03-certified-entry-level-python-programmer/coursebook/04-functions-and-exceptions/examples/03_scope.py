"""4.1.5 - Scope: local, global, shadowing, global keyword."""

rate = 0.2


def tax(amount):
    result = amount * rate
    return result


print(tax(100))                    # -> 20.0
try:
    print(result)
except NameError as e:
    print(e)                       # -> name 'result' is not defined

for i in range(3):
    inside = i
print(i, inside)                   # -> 2 2

x = 10


def shadow():
    x = 99
    print("in f:", x)


shadow()                           # -> in f: 99
print("global:", x)                # -> global: 10

count = 0


def bad_increment():
    count = count + 1


try:
    bad_increment()
except UnboundLocalError as e:
    print(type(e).__name__, isinstance(e, NameError))  # -> UnboundLocalError True


def increment():
    global count
    count += 1


increment()
increment()
print(count)                       # -> 2


def setup():
    global config
    config = "ready"


setup()
print(config)                      # -> ready

items = []


def add(v):
    items.append(v)


add(1)
print(items)                       # -> [1]


def outer():
    msg = "hi"

    def inner():
        return msg
    return inner()


print(outer())                     # -> hi
