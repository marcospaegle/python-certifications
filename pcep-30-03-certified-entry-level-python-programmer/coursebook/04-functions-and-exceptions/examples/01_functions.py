"""4.1.1 / 4.1.2 - Defining, calling, return."""

try:
    say_hi()
except NameError as e:
    print(e)                       # -> name 'say_hi' is not defined


def say_hi():
    print("hi")


say_hi()                           # -> hi


def a():
    b()


def b():
    print("b")


a()                                # -> b


def f():
    return 1


def f():
    return 2


print(f())                         # -> 2


def no_return():
    x = 1


def bare_return():
    return


print(no_return(), bare_return())  # -> None None


def p(x):
    print(x * 2)


def r(x):
    return x * 2


res_p = p(5)                       # -> 10
res_r = r(5)
print(res_p, res_r)                # -> None 10


def first_negative(nums):
    for n in nums:
        if n < 0:
            return n
    return None


print(first_negative([3, -1, -5]), first_negative([1]))  # -> -1 None


def min_max(nums):
    return min(nums), max(nums)


lo, hi = min_max([3, 9, 1])
print(lo, hi, min_max([3, 9, 1]))  # -> 1 9 (1, 9)

double = r
print(double(4))                   # -> 8


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))                # -> 120
