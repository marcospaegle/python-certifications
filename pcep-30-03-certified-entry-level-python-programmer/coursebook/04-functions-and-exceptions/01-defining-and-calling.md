# 4.1a Defining and Calling Functions; `return`

**Objectives covered:** `4.1.1`, `4.1.2`
**Exam section:** 4 – Functions and Exceptions (20%, 7 items)

### What the exam expects (official syllabus, paraphrased)
- [ ] **4.1.1** – How functions support decomposition, reuse and maintainability
- [ ] **4.1.1** – `def`, valid names, an indented body
- [ ] **4.1.1** – Invoke functions; trace the order of definitions and calls
- [ ] **4.1.2** – `return` a result; assign it and use it in expressions and calls
- [ ] **4.1.2** – Returning vs `print()`ing
- [ ] **4.1.2** – `return` ends the call
- [ ] **4.1.2** – Return multiple values
- [ ] **4.1.2** – Implicit `None`; `None` as "no meaningful result"

---

## 0. Why functions (4.1.1)

- **Decomposition:** a large problem is split into small, named steps, such as `read_scores()`, `compute_average()` and `print_report()`. Each step can be understood and tested on its own.
- **Reuse:** code written once can be called many times with different arguments. This avoids copy-paste duplication.
- **Maintainability:** a fix or change is made in one place, the function body, and every caller benefits. A good name also documents what the code does.

```python
# Without a function: the same logic duplicated
print("=" * 10); print("Report"); print("=" * 10)
print("=" * 10); print("Summary"); print("=" * 10)

# With a function: written once, reused, and changed in one place
def banner(title):
    print("=" * 10)
    print(title)
    print("=" * 10)

banner("Report")
banner("Summary")
```

## 1. Defining a function (4.1.1)

```python
def greet(name):
    """Optional docstring: describes the function."""
    message = "Hello, " + name
    print(message)
```

- `def` is followed by the function name, a parameter list in parentheses, and a colon. The indented block is the body.
- Function names follow the normal identifier rules, plus PEP 8 `snake_case`.
- An empty body needs `pass`.
- **`def` is an executable statement.** Running it creates a function object and binds it to the name. The body **doesn't run** until the function is called.

### Invocation

```python
greet("Ada")       # Hello, Ada   the call runs the body
greet              # just the function object; nothing runs
print(greet)       # <function greet at 0x...>
```

### Order of execution

A function must be **defined before it's called** (at the time the call executes):

```python
say_hi()           # NameError: name 'say_hi' is not defined

def say_hi():
    print("hi")
```

A function body may refer to another function that's defined *later*, as long as that function exists by the time the call actually happens:

```python
def a():
    b()            # fine: b is looked up when a() runs

def b():
    print("b")

a()                # b
```

Tracing execution order:

```python
print("1")
def f():
    print("3")
print("2")
f()
print("4")
# 1 2 3 4
```

Redefining a function name replaces the previous definition:

```python
def f(): return 1
def f(): return 2
print(f())         # 2
```

## 2. `return` (4.1.2)

`return expr` ends the function **immediately** and hands `expr` back to the caller.

```python
def square(x):
    return x * x

result = square(4)     # 16
print(square(3) + 1)   # 10
```

### Implicit `None`

A function without `return`, or with a bare `return`, returns **`None`**:

```python
def no_return():
    x = 1

def bare_return():
    return

print(no_return())     # None
print(bare_return())   # None
```

### `None` as "no meaningful result"

Return `None` on purpose to signal that there's nothing to return, for example when a search found nothing. The caller tests for it with **`is None`**:

```python
def find_index(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return None            # explicit: "not found"

pos = find_index(["a", "b"], "z")
if pos is None:
    print("not found")     # printed
```

Test with `is None` rather than truthiness: `if not pos:` would also treat a valid result of `0` as "not found". Using a `None` result in arithmetic raises `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`.

### Using returned values in expressions and calls

```python
def square(x):
    return x * x

total = square(2) + square(3)    # 13
print(square(square(2)))         # 16  (a return value passed as an argument)
```

### `return` vs `print()`

`print` writes to the console; `return` produces a value. They're independent:

```python
def p(x):
    print(x * 2)

def r(x):
    return x * 2

a = p(5)     # prints 10; a is None
b = r(5)     # prints nothing; b is 10
print(a, b)  # None 10
print(p(1))  # prints 2, then None
```

### Early termination

Code after an executed `return` doesn't run, which includes the rest of any loop:

```python
def first_negative(nums):
    for n in nums:
        if n < 0:
            return n        # leaves the loop AND the function
    return None             # reached only when no negative was found

print(first_negative([3, -1, -5]))  # -1
```

```python
def f():
    return 1
    print("never")          # unreachable
```

### Multiple `return` statements

```python
def sign(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    return "zero"
```

### Returning several values

`return a, b` returns **one tuple**:

```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 9, 1])   # unpacked: 1 9
pair = min_max([3, 9, 1])     # (1, 9)
```

### Functions are values *(beyond the syllabus)*

```python
def double(x):
    return x * 2
f = double            # no parentheses: f refers to the same function
print(f(4))           # 8
```

### Recursion *(beyond the syllabus)*

A function can call itself, and it needs a base case:

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120
```

Without a base case you get `RecursionError: maximum recursion depth exceeded`.

---

## Exam traps
- Calling a function before its `def` has executed raises `NameError`.
- The body runs only when the function is called. Referencing `f` without `()` doesn't call it.
- No `return` means the function returns `None`, so `x = print_something()` makes `x` `None`.
- `return` inside a loop exits the whole function.
- `return a, b` returns a tuple.
- Code after `return` is dead code.

## Key takeaways
- `def` creates the function object; a call executes it.
- `return` ends the call and produces its value, which is `None` by default.
- Printing and returning are different things.
