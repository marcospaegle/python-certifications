"""1.4.1 - Operators, precedence, associativity."""

# Division family
print(6 / 2, 7 / 2)                # -> 3.0 3.5
print(7 // 2, -7 // 2, 7 // -2)    # -> 3 -4 -4
print(7.0 // 2, -7.5 // 2)         # -> 3.0 -4.0
print(7 % 3, -7 % 3, 7 % -3, -7 % -3)  # -> 1 2 -2 -1
print(7.5 % 2, 3 % 7)              # -> 1.5 3

# Exponentiation
print(2 ** 3, 2 ** -1, 2.0 ** 3)   # -> 8 0.5 8.0

# String operators
print("ab" + "cd", "ab" * 3, 3 * "-")  # -> abcd ababab ---
print(repr("x" * 0), repr("x" * -2))   # -> '' ''
print("5" + "5")                   # -> 55

# Augmented assignment
x = 10
x += 5
x -= 3
x *= 2
x /= 5
print(x)                           # -> 4.8
x = 2
x *= 2 + 3
print(x)                           # -> 10

# Unary
print(-(-3), - - 3, not 0)         # -> 3 3 True

# Comparisons
print(3 == 3.0, "Z" < "a", "10" < "9", 1 == "1")  # -> True True True False
x = 5
print(1 < x < 10, 1 < x > 3)       # -> True True

# Logical operators return operands
print(0 and 5, 3 and 5, 0 or 5)    # -> 0 5 5
print("" or "default", None or 0)  # -> default 0
print(not "")                      # -> True
x = 0
print(x != 0 and 10 / x > 1)       # -> False

# Precedence traps
print(2 ** 3 ** 2, (2 ** 3) ** 2)  # -> 512 64
print(-2 ** 2, (-2) ** 2)          # -> -4 4
print(10 - 4 - 3, 100 / 10 / 5)    # -> 3 2.0
print(2 + 3 * 4, 10 - 2 * 3 ** 2)  # -> 14 -8
print(7 // 2 * 2, 7 % 4 * 3)       # -> 6 9
print(not 1 == 2)                  # -> True
print(True or False and False)     # -> True
