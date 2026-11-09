"""1.3.1 / 1.3.2 - Literals and variables."""

# Integer literals
print(1_000_000)                   # -> 1000000
print(0b1010, 0o17, 0x1F)          # -> 10 15 31
print(bin(10), oct(15), hex(31))   # -> 0b1010 0o17 0x1f
print(2 ** 100)                    # -> 1267650600228229401496703205376

# Float literals
print(.5, 5., 1e3, 3E-2)           # -> 0.5 5.0 1000.0 0.03
print(type(1e3))                   # -> <class 'float'>
print(0.1 + 0.2)                   # -> 0.30000000000000004
print(0.1 + 0.2 == 0.3)            # -> False
print(1e16, 0.00001)               # -> 1e+16 1e-05

# Booleans are ints
print(True + True, True + 5)       # -> 2 6
print(isinstance(True, int))       # -> True

# Truthiness
print(bool(""), bool("0"), bool([]), bool([0]), bool(-1))  # -> False True False True True

# Reference semantics
a = [1, 2, 3]
b = a
b.append(4)
print(a)                           # -> [1, 2, 3, 4]
print(a is b)                      # -> True

x = 5
y = x
x = x + 1
print(x, y)                        # -> 6 5

# Multiple assignment and swap
p, q = 1, 2
p, q = q, p
print(p, q)                        # -> 2 1

try:
    m, n = 1, 2, 3
except ValueError as e:
    print(e)                       # -> too many values to unpack (expected 2)
