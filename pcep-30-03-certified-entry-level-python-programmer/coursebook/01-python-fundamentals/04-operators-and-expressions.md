# 1.4a Operators and Expressions

**Objectives covered:** `1.4.1`
**Exam section:** 1 – Computer Programming and Python Fundamentals

### What the exam expects (official syllabus, paraphrased)
- Numeric operators `**` `*` `/` `%` `//` `+` `-`
- `+` and `*` with strings
- Assignment and augmented assignment
- Unary vs binary operators
- Precedence, associativity and binding
- Boolean operators `not`, `and`, `or`; constructing and evaluating Boolean expressions
- Relational operators `==` `!=` `>` `>=` `<` `<=`

This is one of the most heavily tested areas, because precedence and division rules generate many "what's the output?" questions.

---

## 1. Arithmetic operators

| Op | Meaning | `7 ? 2` | Result type |
|---|---|---|---|
| `+` | addition | `9` | int if both ints, else float |
| `-` | subtraction | `5` | same |
| `*` | multiplication | `14` | same |
| `/` | **true division** | `3.5` | **always float** |
| `//` | **floor division** | `3` | int if both ints, else float |
| `%` | modulo (remainder) | `1` | int if both ints, else float |
| `**` | exponentiation | `49` | see below |

### 1.1 `/` always returns a float

```python
print(6 / 2)     # 3.0   (not 3)
print(7 / 2)     # 3.5
```

### 1.2 `//` floors toward negative infinity

Floor division rounds **down**, not toward zero:

```python
print(7 // 2)      # 3
print(-7 // 2)     # -4   (−3.5 floors to −4)
print(7 // -2)     # -4
print(7.0 // 2)    # 3.0  (a float operand gives a float result, still floored)
print(-7.5 // 2)   # -4.0
```

### 1.3 `%` takes the sign of the divisor

Python guarantees `a == (a // b) * b + (a % b)`. Because `//` floors, the remainder **has the same sign as the divisor**:

```python
print(7 % 3)      # 1
print(-7 % 3)     # 2    (−7 // 3 = −3; −3*3 = −9; −7 − (−9) = 2)
print(7 % -3)     # -2
print(-7 % -3)    # -1
print(7.5 % 2)    # 1.5
print(3 % 7)      # 3    (smaller dividend: the remainder is the dividend itself)
```

### 1.4 `**` exponentiation

```python
print(2 ** 3)      # 8
print(2 ** -1)     # 0.5    (a negative exponent gives a float)
print(2 ** 0.5)    # 1.4142135623730951
print(2.0 ** 3)    # 8.0
```

### 1.5 Division by zero

`/`, `//` and `%` with a zero divisor raise `ZeroDivisionError`, for ints and floats alike: `5 / 0`, `5 // 0`, `5 % 0` and `5.0 / 0` all raise it.

### 1.6 Mixed types

int combined with float gives float: `3 + 2.0` → `5.0`. bool behaves as int: `True * 10` → `10`.

## 2. String operators

```python
print("ab" + "cd")    # abcd    concatenation (both operands must be str)
print("ab" * 3)       # ababab  replication (str * int or int * str)
print(3 * "-")        # ---
print("x" * 0)        # ''  (empty)
print("x" * -2)       # ''  (negative counts give an empty string)
```

```python
"a" + 1      # TypeError: can only concatenate str (not "int") to str
"a" * 2.0    # TypeError: can't multiply sequence by non-int of type 'float'
"5" + "5"    # '55'   (not 10)
```

The same `+` and `*` behaviour applies to lists and tuples: `[0] * 3` → `[0, 0, 0]`.

## 3. Assignment and augmented assignment

```python
x = 10
x += 5     # x = x + 5   -> 15
x -= 3     # 12
x *= 2     # 24
x /= 5     # 4.8   (float now!)
x //= 2    # 2.0
x %= 2     # 0.0
x **= 3    # 0.0
s = "ab"
s *= 2     # 'abab'
```

- There's **no `++` or `--` operator**. `x++` is a `SyntaxError`, while `++x` is legal and means `+(+x)`, which is just `x`.
- In `x *= 2 + 3` the whole right side is evaluated first, so it means `x = x * (2 + 3)`.

## 4. Unary vs binary operators

- **Binary** operators take two operands: `a - b`.
- **Unary** operators take one: `-x`, `+x`, `not x`. (Bitwise `~x` is also unary, but bitwise operators aren't in the 30-03 syllabus.)

```python
print(-(-3))     # 3
print(- - 3)     # 3
print(not 0)     # True
```

## 5. Relational (comparison) operators

`==`, `!=`, `<`, `<=`, `>`, `>=` always return `bool`.

```python
print(3 == 3.0)        # True   (numeric value equality across int and float)
print("a" < "b")       # True   (strings compare lexicographically by code point)
print("Z" < "a")       # True   (uppercase letters have lower code points than lowercase)
print("10" < "9")      # True   ('1' < '9': string comparison, not numeric)
print(1 == "1")        # False  (no implicit conversion)
print(1 < "2")         # TypeError: '<' not supported between instances of 'int' and 'str'
```

**Chained comparisons** work like mathematical notation: `a < b < c` means `a < b and b < c`, and `b` is evaluated only once.

```python
x = 5
print(1 < x < 10)    # True
print(1 < x > 3)     # True  (1 < 5 and 5 > 3)
print(3 == 3 == 3.0) # True
```

`=` is assignment; `==` is comparison.

## 6. Logical operators: `not`, `and`, `or`

| Expression | Returns |
|---|---|
| `not x` | `True` if `x` is falsy, else `False` (always a bool) |
| `x and y` | `x` if `x` is falsy, **otherwise `y`** |
| `x or y` | `x` if `x` is truthy, **otherwise `y`** |

`and` and `or` **short-circuit** and **return one of their operands**, not necessarily a bool:

```python
print(True and False)   # False
print(0 and 5)          # 0     (0 is falsy, so it's returned without evaluating 5)
print(3 and 5)          # 5
print(0 or 5)           # 5
print("" or "default")  # default
print(None or 0)        # 0
print(not "")           # True
```

Short-circuit evaluation means the right operand may never be evaluated:

```python
x = 0
print(x != 0 and 10 / x > 1)   # False, no ZeroDivisionError
```

## 7. Precedence and associativity

From **highest** to **lowest**, for the operators on the syllabus:

| Precedence | Operators | Associativity |
|---|---|---|
| 1 | `( )` parentheses | — |
| 2 | `**` | **right-to-left** |
| 3 | unary `+x`, `-x` | — |
| 4 | `*`, `/`, `//`, `%` | left-to-right |
| 5 | binary `+`, `-` | left-to-right |
| 6 | `==`, `!=`, `<`, `<=`, `>`, `>=`, `in`, `not in`, `is`, `is not` | chained |
| 7 | `not` | — |
| 8 | `and` | left-to-right |
| 9 | `or` | left-to-right |
| 10 | `:=` (walrus) | — |

Assignment (`=`, `+=`) is a statement, not an operator in this table.

### The famous traps

```python
print(2 ** 3 ** 2)     # 512   = 2 ** (3 ** 2) = 2 ** 9       (right-assoc)
print((2 ** 3) ** 2)   # 64
print(-2 ** 2)         # -4    = -(2 ** 2): ** binds tighter than unary minus
print((-2) ** 2)       # 4
print(2 ** -1)         # 0.5   unary minus on the RIGHT of ** is fine
print(10 - 4 - 3)      # 3     (10-4)-3 left-assoc
print(100 / 10 / 5)    # 2.0   (100/10)/5
print(2 + 3 * 4)       # 14
print(10 - 2 * 3 ** 2) # -8    3**2=9; 2*9=18; 10-18
print(7 // 2 * 2)      # 6     same level, left to right: (7//2)*2
print(7 % 4 * 3)       # 9     (7%4)*3
print(not 1 == 2)      # True  = not (1 == 2)
print(True or False and False)  # True  = True or (False and False)
```

---

## Exam traps
- `/` always gives a float: `4 / 2` is `2.0`.
- `-7 // 2` is `-4`, and `-7 % 3` is `2`.
- `**` is right-associative, and `-2 ** 2` is `-4`.
- `*`, `/`, `//` and `%` share one precedence level and evaluate left to right.
- `and` and `or` return operands: `0 or ""` returns `""`.
- `and` binds tighter than `or`.
- `"10" < "9"` is `True`.
- There's no `++`.

## Key takeaways
- Know the result type of every arithmetic operator by heart.
- Floor division and modulo follow the floor rule, which affects negative numbers.
- Memorize the precedence table, especially where `**`, unary minus, `not`, `and` and `or` sit.
