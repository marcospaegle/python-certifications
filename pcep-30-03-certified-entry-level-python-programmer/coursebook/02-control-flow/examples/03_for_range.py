"""2.2.2 / 2.2.3 - for loops and range()."""

for ch in "abc":
    print(ch, end=" ")
print()                            # -> a b c

for key in {"a": 1, "b": 2}:
    print(key, end=" ")
print()                            # -> a b

for i in range(3):
    print(i, end=" ")
    i = 100                        # no effect on iteration
print()                            # -> 0 1 2

for i in range(5):
    pass
print(i)                           # -> 4

total = 0
for n in [4, 7, 1]:
    total += n
print(total)                       # -> 12

word = ""
for ch in "abc":
    word = ch + word
print(word)                        # -> cba

print(list(range(5)))              # -> [0, 1, 2, 3, 4]
print(list(range(2, 6)))           # -> [2, 3, 4, 5]
print(list(range(0, 10, 3)))       # -> [0, 3, 6, 9]
print(list(range(5, 5)), list(range(5, 2)))  # -> [] []
print(list(range(5, 0, -1)))       # -> [5, 4, 3, 2, 1]
print(list(range(5, -1, -1)))      # -> [5, 4, 3, 2, 1, 0]
print(list(range(10, 0, -3)))      # -> [10, 7, 4, 1]
print(list(range(0, 5, -1)))       # -> []
print(len(range(0, 10, 3)))        # -> 4
print(range(3))                    # -> range(0, 3)

try:
    range(0, 5, 0)
except ValueError as e:
    print(e)                       # -> range() arg 3 must not be zero

try:
    for i in 5:
        pass
except TypeError as e:
    print(e)                       # -> 'int' object is not iterable
