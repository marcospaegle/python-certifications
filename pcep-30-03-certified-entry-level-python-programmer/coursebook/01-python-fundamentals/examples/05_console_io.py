"""1.4.2 - print(), input(), type conversion.

Run interactively:   python3 05_console_io.py
Or with piped input: printf '4\n7\n' | python3 05_console_io.py
"""

print("a", "b", 3)                 # -> a b 3
print("a", "b", sep="-")           # -> a-b
print("no newline", end="")
print("!")                         # -> no newline!
print(1, 2, 3, sep=", ", end=".\n")  # -> 1, 2, 3.
print("a", "b", "-")               # -> a b -

# Conversions
print(int("  42  "), int(3.99), int(-3.99), int(True))  # -> 42 3 -3 1
print(int("ff", 16), int("1_000"))  # -> 255 1000
print(float("1e3"), float(7))      # -> 1000.0 7.0
print(str(3.0), bool("False"))     # -> 3.0 True
print(round(2.5), round(3.5), round(7.456, 1))  # -> 2 4 7.5

try:
    int("3.5")
except ValueError as e:
    print(e)                       # -> invalid literal for int() with base 10: '3.5'
print(int(float("3.5")))           # -> 3

# input -> process -> output
a = float(input("First number: "))
b = float(input("Second number: "))
total = a + b
print("Sum:", total)
print("Average:", total / 2)
