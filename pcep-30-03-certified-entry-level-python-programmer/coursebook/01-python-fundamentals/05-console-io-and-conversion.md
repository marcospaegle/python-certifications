# 1.4b Console Input/Output and Type Conversion

**Objectives covered:** `1.4.2`
**Exam section:** 1 – Computer Programming and Python Fundamentals

### What the exam expects (official syllabus, paraphrased)
- [ ] **1.4.2** – Display values with `print()`
- [ ] **1.4.2** – Read input with `input()`, which returns a string
- [ ] **1.4.2** – Convert with `int()`, `float()`, `str()`
- [ ] **1.4.2** – Convert input before processing it
- [ ] **1.4.2** – Combine input, conversion, processing and output in a simple program

---

## 1. `print()`

Signature (simplified): `print(*objects, sep=' ', end='\n')`

- It takes **any number** of arguments of any type, converts each with `str()`, joins them with `sep` and writes `end` after the last one.
- It returns `None`.

```python
print("a", "b", 3)            # a b 3
print("a", "b", sep="-")      # a-b
print("a", "b", sep="")       # ab
print("no newline", end="")
print("!")                    # no newline!
print()                       # prints just an empty line
print("x", end=" | "); print("y")   # x | y
print(1, 2, 3, sep=", ", end=".\n") # 1, 2, 3.
```

- `sep` and `end` **must be passed as keyword arguments**. `print("a", "b", "-")` just prints three objects: `a b -`.
- `print(print("x"))` prints `x`, then `None`.
- `\n` inside a string creates a line break: `print("a\nb")` prints two lines.

## 2. `input()`

Signature: `input(prompt='')`

- It writes the prompt (with no newline added), reads one line from standard input, strips the trailing newline, and **always returns a `str`**.

```python
name = input("Name: ")         # user types: Ada
print("Hello,", name)          # Hello, Ada

age = input("Age: ")           # user types: 30
print(age + 1)                 # TypeError: can only concatenate str (not "int") to str
print(age * 2)                 # 3030  (string replication!)
print(int(age) + 1)            # 31
```

## 3. Type conversion functions

### `int(x)`
```python
int("42")       # 42
int("  42  ")   # 42     (surrounding whitespace is ignored)
int("-7")       # -7
int(3.99)       # 3      (truncates toward zero, it doesn't round)
int(-3.99)      # -3
int(True)       # 1
int("3.5")      # ValueError: invalid literal for int() with base 10: '3.5'
int("abc")      # ValueError
int("")         # ValueError
int("1_000")    # 1000   (underscores follow literal rules)
int("ff", 16)   # 255    (optional base argument)
```

### `float(x)`
```python
float("3.5")    # 3.5
float("  2 ")   # 2.0
float(7)        # 7.0
float("1e3")    # 1000.0
float("abc")    # ValueError: could not convert string to float: 'abc'
```

### `str(x)`
```python
str(42)         # '42'
str(3.0)        # '3.0'
str(True)       # 'True'
str(None)       # 'None'
```

### `bool(x)`
This returns the truthiness of `x`: `bool("False")` is `True` (a non-empty string). `bool(0.0)` is `False`.

### Rounding vs truncating
`int()` truncates toward zero. `round()` rounds to the nearest value, and **ties go to the even neighbour** (banker's rounding):

```python
round(2.5)    # 2
round(3.5)    # 4
round(2.675, 2)  # 2.67  (float representation, not a bug)
round(7.456, 1)  # 7.5
```

## 4. The input → process → output pattern

```python
# Read two numbers, print their sum and average
a = float(input("First number: "))
b = float(input("Second number: "))
total = a + b
print("Sum:", total)
print("Average:", total / 2)
```

Example run:

```text
First number: 4
Second number: 7
Sum: 11.0
Average: 5.5
```

Nested conversion is idiomatic: `int(input())`. The outer conversion fails with `ValueError` if the user types something that isn't numeric.

---

## Exam traps
- `input()` returns `str`, so `input() + 1` gives a `TypeError`, and `input() * 2` repeats the string.
- `int("3.5")` raises `ValueError`. Use `int(float("3.5"))` → `3`.
- `int(3.99)` is `3`: it truncates.
- `round(2.5)` is `2`.
- `print()` returns `None`.
- The `sep` and `end` defaults are `' '` and `'\n'`.
- `print("a", "b", sep="")` prints `ab`.

## Key takeaways
- `print` joins its arguments with `sep` and ends with `end`.
- `input` always produces a string, so convert it explicitly with `int()` or `float()`.
- An invalid conversion raises `ValueError`.
