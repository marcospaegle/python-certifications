"""5.1.1 - File modes, with, reading, writing, appending, errors.

Creates a temporary file "_demo.txt" next to this script and deletes it at the end.
"""
import os

PATH = "_demo.txt"

# "w" creates/truncates; write() adds no newline and returns the char count
with open(PATH, "w", encoding="utf-8") as f:
    f.write("alpha\n")
    f.write("beta\n")
    n = f.write("gamma\n")
print(n)                           # -> 6

with open(PATH, encoding="utf-8") as f:   # default mode "r"
    print(repr(f.read()))          # -> 'alpha\nbeta\ngamma\n'

with open(PATH, encoding="utf-8") as f:
    print(repr(f.readline()), repr(f.readline()))  # -> 'alpha\n' 'beta\n'

with open(PATH, encoding="utf-8") as f:
    print(f.readlines())           # -> ['alpha\n', 'beta\n', 'gamma\n']

with open(PATH, encoding="utf-8") as f:
    for line in f:
        print(line.strip(), end=" ")
print()                            # -> alpha beta gamma

with open(PATH, encoding="utf-8") as f:
    first = f.read()
    second = f.read()
print(repr(second))                # -> ''

# "a" appends
with open(PATH, "a", encoding="utf-8") as f:
    f.write("delta\n")
with open(PATH, encoding="utf-8") as f:
    print(len(f.readlines()))      # -> 4

# "w" truncates even if nothing is written
with open(PATH, "w", encoding="utf-8") as f:
    pass
print(os.path.getsize(PATH))       # -> 0

# Errors
try:
    open("does_not_exist.txt")
except FileNotFoundError as e:
    print(type(e).__name__, isinstance(e, OSError))  # -> FileNotFoundError True

with open(PATH, "w", encoding="utf-8") as f:
    try:
        f.write(42)
    except TypeError as e:
        print(e)                   # -> write() argument must be str, not int

try:
    f.read()
except ValueError as e:
    print(e)                       # -> I/O operation on closed file.

os.remove(PATH)
