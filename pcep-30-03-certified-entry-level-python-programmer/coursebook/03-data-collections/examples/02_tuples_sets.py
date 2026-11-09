"""3.2.1 / 3.3.1 - Tuples and sets."""

# Tuples
print(type((5)), type((5,)))       # -> <class 'int'> <class 'tuple'>
packed = 1, 2, 3
print(packed, len(()))             # -> (1, 2, 3) 0
t = (10, 20, 30, 40)
print(t[0], t[-1], t[1:3], t[::-1])  # -> 10 40 (20, 30) (40, 30, 20, 10)
print(sorted((3, 1, 2)))           # -> [1, 2, 3]

try:
    t[0] = 99
except TypeError as e:
    print(e)                       # -> 'tuple' object does not support item assignment

t = (1, 2)
t += (3,)
print(t)                           # -> (1, 2, 3)

t = (1, [2, 3])
t[1].append(4)
print(t)                           # -> (1, [2, 3, 4])

x, y = (3, 4)
print(x, y)                        # -> 3 4

# Sets
print({3, 1, 3, 2, 1} == {1, 2, 3}, len({1, 1, 1}))  # -> True 1
print(type({}), type(set()))       # -> <class 'dict'> <class 'set'>
print({1, True}, len({0, False, 1}))  # -> {1} 2

s = {1, 2}
s.add(3)
s.add(2)
s.update([4, 5])
s.discard(10)
s.remove(1)
print(sorted(s))                   # -> [2, 3, 4, 5]

try:
    s.remove(10)
except KeyError as e:
    print("KeyError", e)           # -> KeyError 10

try:
    s[0]
except TypeError as e:
    print(e)                       # -> 'set' object is not subscriptable

try:
    {[1, 2]}
except TypeError as e:
    print(e)                       # -> unhashable type: 'list'

print("e" in {"a", "e"}, len(set(["a", "b", "a", "c", "b"])))  # -> True 3
a, b = {1, 2, 3}, {2, 3, 4}
print(sorted(a | b), sorted(a & b), a - b, sorted(a ^ b))  # -> [1, 2, 3, 4] [2, 3] {1} [1, 4]
