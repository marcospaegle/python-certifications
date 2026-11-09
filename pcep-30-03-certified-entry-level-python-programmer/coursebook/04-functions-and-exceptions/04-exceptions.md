# 4.2 Exceptions

**Objectives covered:** `4.2.1`, `4.2.2`
**Exam section:** 4 – Functions and Exceptions

### What the exam expects (official syllabus, paraphrased)
- [ ] **4.2.1** – The purpose of exceptions; how they interrupt the flow
- [ ] **4.2.1** – Common situations that raise them
- [ ] **4.2.1** – `ValueError`, `TypeError`, `ZeroDivisionError`, `IndexError`, `KeyError`, `NameError`, and the operations that cause each
- [ ] **4.2.2** – `try` / `except` for runtime exceptions
- [ ] **4.2.2** – One or more specific `except` branches
- [ ] **4.2.2** – Trace the flow when an exception does and doesn't occur

---

## 1. What exceptions are (4.2.1)

An **exception** is an object that signals an error at runtime. When one is **raised**:

1. Normal execution stops **at that point**. The rest of the current block is skipped.
2. Python looks for a matching handler (`except`) in the current function, then in its caller, then in *that* caller, and so on up the call stack.
3. If no handler is found, the program terminates and prints a **traceback**:

```text
Traceback (most recent call last):
  File "demo.py", line 2, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero
```

The last line holds the exception **type** and **message**. Output printed before the error still appears.

## 2. Common built-in exceptions

| Exception | Raised when | Example |
|---|---|---|
| `ValueError` | the right type but an inappropriate value | `int("abc")`, `[1, 2].index(5)`, `a, b = [1, 2, 3]` |
| `TypeError` | an operation is applied to the wrong type | `"a" + 1`, `len(5)`, `None + 1`, calling with the wrong number of arguments |
| `ZeroDivisionError` | division or modulo by zero | `1 / 0`, `5 // 0`, `5 % 0` |
| `IndexError` | a sequence index is out of range | `[1, 2][5]`, `"ab"[2]`, `[].pop()` |
| `KeyError` | a dict key (or set element for `remove`) is missing | `{"a": 1}["b"]`, `set().remove(1)` |
| `NameError` | a name isn't defined | `print(undefined_var)`, a misspelled function name |

Others you'll meet: `AttributeError` (`(1, 2).append(3)`), `SyntaxError` and `IndentationError` (at compile time, which `try` can't catch in the same file), `FileNotFoundError` (Chapter 5), `RecursionError`, `UnboundLocalError` (a subclass of `NameError`) and `KeyboardInterrupt`.

### The hierarchy (only what you need)

```text
BaseException
 ├── KeyboardInterrupt
 └── Exception
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── NameError
      │    └── UnboundLocalError
      ├── TypeError
      ├── ValueError
      └── OSError
           └── FileNotFoundError
```

A handler for a parent class also catches all of its subclasses. For example, `except LookupError:` catches both `IndexError` and `KeyError`.

## 3. `try` / `except` (4.2.2)

```python
try:
    risky_code()
except SomeError:
    handle_it()
```

- If no exception occurs, the `except` blocks are skipped.
- If an exception occurs, the rest of the `try` block is **skipped**. The first matching `except` runs, and then execution continues **after the whole statement**.
- If no `except` matches, the exception propagates outward as if there were no `try`.

```python
try:
    print("A")
    x = 1 / 0
    print("B")          # skipped
except ZeroDivisionError:
    print("C")
print("D")
# A C D
```

### Specific handlers and access to the exception

```python
try:
    n = int(input("Number: "))
    print(10 / n)
except ValueError:
    print("Not a number")
except ZeroDivisionError as e:
    print("Error:", e)     # Error: division by zero
```

`as e` binds the exception object; `str(e)` is its message.

### Multiple exceptions in one handler

Use a **tuple**:

```python
try:
    ...
except (ValueError, TypeError):
    print("bad input")
```

### Bare `except` / `except Exception`

```python
try:
    ...
except:              # catches EVERYTHING (even KeyboardInterrupt); discouraged
    ...
```

A bare `except:` **must be the last** handler, or you get `SyntaxError: default 'except:' must be last`.

### Order matters: the first match wins

Handlers are tested top to bottom, so put **specific exceptions before general ones**:

```python
try:
    [1, 2][5]
except LookupError:
    print("lookup")      # runs: IndexError is a LookupError
except IndexError:
    print("index")       # never reached
```

### `else` and `finally` *(beyond the syllabus)*

```python
try:
    value = int("42")
except ValueError:
    print("bad")
else:
    print("ok", value)      # runs only if NO exception occurred
finally:
    print("always")         # runs no matter what, even after return or an unhandled error
# ok 42
# always
```

## 4. Tracing exception flow across functions

```python
def level2():
    print("L2 start")
    return 1 / 0
    print("L2 end")         # never runs

def level1():
    print("L1 start")
    level2()
    print("L1 end")         # skipped: the exception passes through

try:
    level1()
except ZeroDivisionError:
    print("caught in main")
print("program continues")
# L1 start
# L2 start
# caught in main
# program continues
```

An exception raised **inside an `except` block** isn't caught by the sibling handlers of the same `try`:

```python
try:
    int("x")
except ValueError:
    print(1 / 0)        # ZeroDivisionError propagates; the next handler doesn't apply
except ZeroDivisionError:
    print("not here")
```

### Raising exceptions *(beyond the syllabus)*

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("insufficient funds")
    return balance - amount
```

A bare `raise` inside an `except` block re-raises the current exception.

### Validation loop pattern

```python
while True:
    try:
        age = int(input("Age: "))
        break
    except ValueError:
        print("Please enter a whole number.")
```

---

## Exam traps
- After an exception, the rest of the `try` block is skipped, but code after the whole `try` statement runs once the exception is handled.
- Only the **first** matching `except` runs. Specific handlers must come before general ones.
- A bare `except:` must be last.
- To catch several exceptions in one handler, use a tuple: `except (A, B):`.
- `else` runs only when there was no exception; `finally` always runs.
- An unhandled exception propagates up through the callers, skipping the rest of each function.
- `int("3.5")` raises `ValueError`, not `TypeError`. `"a" + 1` raises `TypeError`.
- `d["missing"]` raises `KeyError`, while `lst[99]` raises `IndexError`.

## Key takeaways
- Exceptions interrupt normal flow and travel up the call stack until something handles them.
- `try/except` catches them, with handlers tested top to bottom.
- Know the six core exceptions and exactly which operations raise each one.
