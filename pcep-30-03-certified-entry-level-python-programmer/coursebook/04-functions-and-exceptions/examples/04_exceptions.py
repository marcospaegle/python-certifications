"""4.2.1 / 4.2.2 - Exceptions and try/except."""

# Each `lambda: ...` is a tiny anonymous function. It delays running the
# expression until case() is called inside the try block below.
cases = [
    lambda: int("abc"),
    lambda: "a" + 1,
    lambda: 1 / 0,
    lambda: [1, 2][5],
    lambda: {"a": 1}["b"],
    lambda: undefined_name,  # noqa: F821
]
for case in cases:
    try:
        case()
    except Exception as e:
        print(type(e).__name__)
# -> ValueError
# -> TypeError
# -> ZeroDivisionError
# -> IndexError
# -> KeyError
# -> NameError

try:
    print("A")
    x = 1 / 0
    print("B")
except ZeroDivisionError:
    print("C")
print("D")
# -> A
# -> C
# -> D

try:
    [1, 2][5]
except LookupError:
    print("lookup")                # -> lookup
except IndexError:
    print("index")

try:
    int("x")
except (ValueError, TypeError) as e:
    print("bad input:", e)         # -> bad input: invalid literal for int() with base 10: 'x'

try:
    value = int("42")
except ValueError:
    print("bad")
else:
    print("ok", value)             # -> ok 42
finally:
    print("always")                # -> always


def level2():
    print("L2 start")
    return 1 / 0


def level1():
    print("L1 start")
    level2()
    print("L1 end")


try:
    level1()
except ZeroDivisionError:
    print("caught in main")
print("program continues")
# -> L1 start
# -> L2 start
# -> caught in main
# -> program continues


def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("insufficient funds")
    return balance - amount


try:
    withdraw(10, 50)
except ValueError as e:
    print(e)                       # -> insufficient funds

# An exception inside an except block is not caught by sibling handlers
try:
    try:
        int("x")
    except ValueError:
        print(1 / 0)
    except ZeroDivisionError:
        print("not here")
except ZeroDivisionError:
    print("caught by the OUTER try")  # -> caught by the OUTER try
