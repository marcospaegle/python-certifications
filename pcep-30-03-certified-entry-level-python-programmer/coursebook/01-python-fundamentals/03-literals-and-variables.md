# 1.3 Literals and Variables

**Objectives covered:** `1.3.1`, `1.3.2`
**Exam section:** 1 – Computer Programming and Python Fundamentals

### What the exam expects (official syllabus, paraphrased)
- Recognize `int`, `float`, `str` and `bool` literals
- Use Boolean literals
- Use integer and floating-point literals
- Explain the limits of floating-point accuracy and representation
- Construct string literals with appropriate quotes
- Create variables and assign values
- Explain how variables reference values
- Select valid and meaningful names
- Distinguish valid and invalid identifiers
- Apply PEP 8 to variable names and assignment statements

---

## 1. Literals

A **literal** is a value written directly in source code. Check any value's type with `type()`.

### 1.1 Integers (`int`)

```python
42          # decimal
-7          # (unary minus applied to the literal 7)
1_000_000   # underscores as visual separators -> 1000000
0b1010      # binary      -> 10
0o17        # octal       -> 15
0x1F        # hexadecimal -> 31
```

- `int` has **arbitrary precision**: `2 ** 100` is exact and never overflows.
- Leading zeros on a non-zero decimal literal are illegal: `07` is a `SyntaxError` (use `0o7`). `00` is legal.
- Underscores may only sit *between* digits: `1__0`, `_1` and `1_` are invalid (and `_1` is actually an identifier).
- Conversion helpers: `bin(10)` → `'0b1010'`, `oct(15)` → `'0o17'`, `hex(31)` → `'0x1f'`.

### 1.2 Floating-point numbers (`float`)

```python
3.14
.5          # 0.5
5.          # 5.0
1e3         # 1000.0   scientific notation always gives a float
3E-2        # 0.03
1_000.5     # 1000.5
```

- A float is an IEEE-754 double: about 15–17 significant digits.
- **Precision limits:** many decimal fractions have no exact binary representation.

```python
print(0.1 + 0.2)          # 0.30000000000000004
print(0.1 + 0.2 == 0.3)   # False
print(round(0.1 + 0.2, 2) == 0.3)  # True
```

- Very large or small values are displayed in exponent form: `print(1e16)` → `1e+16`, `print(0.00001)` → `1e-05`.
- `1e3` is a float even though its value is whole. `type(1e3)` is `<class 'float'>`.

### 1.3 Strings (`str`)

```python
'single'
"double"
'''triple single'''
"""triple double"""   # can span multiple lines
""                    # empty string
```

- Single and double quotes are equivalent. Pick the one that lets you embed the other: `"It's"`, `'He said "hi"'`.
- Escape sequences: `\n`, `\t`, `\\`, `\'`, `\"`. Strings are covered in depth in Chapter 3.
- `"5"` is a **str**, not a number.

### 1.4 Booleans (`bool`)

- There are exactly two: `True` and `False` (capitalized keywords).
- `bool` is a **subclass of `int`**: `True == 1`, `False == 0`, and `True + True == 2`.

```python
print(True + 5)          # 6
print(type(True))        # <class 'bool'>
print(isinstance(True, int))  # True
```

### 1.5 `None`

`None` is the single value of `NoneType`. It means "no value", and it's what a function returns when it has no `return` value.

### 1.6 Truthiness (needed for conditions)

Every object has a Boolean value. These are **falsy**: `False`, `None`, `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`, `range(0)`. **Everything else is truthy**, including `"0"`, `" "`, `"False"`, `[0]` and `-1`.

```python
print(bool(""), bool("0"), bool([]), bool([0]), bool(-1))
# False True False True True
```

## 2. Variables

### 2.1 Assignment and dynamic typing

A variable is created by **assigning** to it. There's no declaration and no type annotation is required.

```python
count = 10
count = "ten"     # legal: the name now refers to a str
```

Types belong to **objects**, not names. A name can be rebound to an object of any type.

Using a name before assigning it raises `NameError`:

```python
print(score)    # NameError: name 'score' is not defined
```

### 2.2 Reference semantics

**A variable is a name bound to an object.** Assignment never copies an object; it binds the name to the object the right-hand side evaluates to.

```python
a = [1, 2, 3]
b = a           # b and a refer to the SAME list
b.append(4)
print(a)        # [1, 2, 3, 4]
```

With **immutable** objects (int, float, str, bool, tuple) this sharing is invisible, because you can't change them. "Changing" them always produces a new object and rebinds the name:

```python
x = 5
y = x
x = x + 1       # creates a new int 6 and rebinds x; y still refers to 5
print(x, y)     # 6 5
```

- `id(obj)` returns an object's identity.
- `a is b` tests whether two names refer to the *same* object. `a == b` tests whether the values are equal. Use `==` for value comparison, and `is` only for `None` (`x is None`).

### 2.3 Multiple and chained assignment

```python
a, b, c = 1, 2, 3        # tuple unpacking (counts must match)
a, b = b, a              # swap: the right side is fully evaluated first
x = y = z = 0            # all three bound to the same object
```

`a, b = 1, 2, 3` raises `ValueError: too many values to unpack (expected 2)`.

### 2.4 Naming rules (enforced by the language)

- A name may contain only letters, digits and underscores.
- It **cannot start with a digit**.
- It **cannot be a keyword**.
- It's **case-sensitive**: `total`, `Total` and `TOTAL` are three different names.
- Unicode letters are allowed (`café = 1`), but stick to ASCII.

```text
valid:   x, _temp, user_name, userName, item2, __private, _
invalid: 2nd_item, user-name, my var, for, total$
```

### 2.5 Naming conventions (PEP 8, not enforced)

| Kind | Convention | Example |
|---|---|---|
| Variables, functions | `snake_case` | `max_value`, `get_total()` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_SIZE = 100` (still reassignable; it's convention only) |
| Classes | `PascalCase` | `BankAccount` |
| Internal / "private" | leading `_` | `_cache` |
| Throwaway | `_` | `for _ in range(3):` |

Avoid single-letter `l`, `O` and `I` (easily confused with `1` and `0`). Avoid shadowing built-ins (`list`, `str`, `sum`).

**Meaningful names:** `total_price` says what the value is, where `tp` or `x1` don't. Single letters are fine only for short-lived counters (`i`, `j`) or math formulas.

### 2.6 PEP 8 for assignment statements

| Recommendation | Good | Bad |
|---|---|---|
| One space on each side of `=` and augmented operators | `x = 5`, `x += 1` | `x=5`, `x +=1` |
| One statement per line | `a = 1` <br> `b = 2` | `a = 1; b = 2` |
| No extra spaces just to align values | `x = 1` <br> `long_name = 2` | `x         = 1` |
| **No** spaces around `=` for keyword arguments and defaults | `print(a, end="")`, `def f(x=0):` | `print(a, end = "")` |
| Spaces around lower-priority operators, to show grouping | `y = a*b + c` (or `y = a * b + c`) | `y=a*b+c` |

PEP 8 is a style guide: violating it never causes an error.

---

## Exam traps
- `07` is a `SyntaxError`; `0o7` is octal 7.
- `1e3` is a `float` (`1000.0`), not an int.
- `0.1 + 0.2 == 0.3` is `False`.
- `True + True` is `2`, because bool is an int.
- `"0"` and `" "` are truthy; `0`, `""` and `[]` are falsy.
- `b = a` with a list makes an alias, not a copy.
- Names are case-sensitive, and `my-var` is parsed as `my - var`.

## Key takeaways
- The core literals are `int` (arbitrary precision, with 0b/0o/0x forms), `float` (IEEE double), `str` and `bool` (a subclass of int).
- Variables are names bound to objects, and assignment never copies.
- Naming rules come from the language; naming conventions come from PEP 8.
