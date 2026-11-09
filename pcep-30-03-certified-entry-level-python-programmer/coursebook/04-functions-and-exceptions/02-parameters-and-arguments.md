# 4.1b Parameters and Arguments

**Objectives covered:** `4.1.3`, `4.1.4`
**Exam section:** 4 – Functions and Exceptions

### What the exam expects (official syllabus, paraphrased)
- [ ] **4.1.3** – Parameters vs arguments
- [ ] **4.1.3** – Positional and keyword arguments, in the correct order
- [ ] **4.1.3** – Default values: use or override them
- [ ] **4.1.3** – `print()`'s `sep` and `end`
- [ ] **4.1.3** – Recognize invalid calls: missing, duplicated or misordered arguments
- [ ] **4.1.4** – `*args` collects extra positional arguments into a tuple; iterate over it
- [ ] **4.1.4** – `**kwargs` collects extra keyword arguments into a dict; process its keys and values
- [ ] **4.1.4** – Combine standard, default, `*args` and `**kwargs` parameters in a valid definition

---

## 1. Parameters vs arguments (4.1.3)

- **Parameters** are the names in the function **definition**: `def area(width, height):`.
- **Arguments** are the values passed at the **call**: `area(3, 4)`.

Parameters behave as local variables, bound to the arguments when the call starts.

## 2. Positional and keyword arguments

```python
def describe(name, age, city):
    print(f"{name}, {age}, {city}")

describe("Ada", 36, "London")                    # positional: matched by order
describe(age=36, city="London", name="Ada")      # keyword: matched by name, any order
describe("Ada", city="London", age=36)           # mixed
```

Rules:
1. **Positional arguments must come before keyword arguments** at the call site.
   `describe(name="Ada", 36, "London")` raises `SyntaxError: positional argument follows keyword argument`.
2. Each parameter gets **exactly one** value.
   `describe("Ada", name="Bob", age=1, city="x")` raises `TypeError: describe() got multiple values for argument 'name'`.
3. Every required parameter needs a value.
   `describe("Ada")` raises `TypeError: describe() missing 2 required positional arguments: 'age' and 'city'`.
4. You can't pass too many arguments, or unknown keywords.
   `describe(1, 2, 3, 4)` raises `TypeError: describe() takes 3 positional arguments but 4 were given`.
   `describe("a", 1, "c", zip=1)` raises `TypeError: describe() got an unexpected keyword argument 'zip'`.

## 3. Default parameter values

```python
def power(base, exp=2):
    return base ** exp

power(3)        # 9
power(3, 3)     # 27
power(exp=0, base=5)  # 1
```

- **Parameters with defaults must come after parameters without them** in the definition. `def f(a=1, b):` is a `SyntaxError: parameter without a default follows parameter with a default`.
- **Defaults are evaluated once, when `def` executes**, not on each call. A mutable default is shared between calls:

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2]   the same list as before!

def add_item_ok(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

## 4. `print()`'s `sep` and `end`

`print` is the built-in example of keyword arguments with defaults:

```python
print("a", "b", sep="")          # ab
print("a", end="")               # no newline afterwards
print("x", "y", "z", sep="-", end="!\n")   # x-y-z!
```

## 5. Arguments are passed by object reference

The parameter is bound to **the same object** the caller passed:
- If the function **mutates** a mutable argument, the caller sees the change.
- If the function **rebinds** the parameter (`param = ...`), the caller doesn't see it.

```python
def modify(lst):
    lst.append(4)        # mutation: visible to the caller

def rebind(lst):
    lst = [0]            # rebinding a local name: invisible

data = [1, 2, 3]
modify(data)
rebind(data)
print(data)              # [1, 2, 3, 4]

def inc(n):
    n += 1               # ints are immutable, so this rebinds locally
x = 5
inc(x)
print(x)                 # 5
```

## 6. `*args` and `**kwargs` (4.1.4)

### `*args`: variable positional arguments

A parameter prefixed with `*` collects any **extra positional arguments** into a **tuple**:

```python
def total(*args):
    print(type(args), args)
    return sum(args)

total()            # <class 'tuple'> ()           -> 0
total(1, 2, 3)     # <class 'tuple'> (1, 2, 3)    -> 6
```

### `**kwargs`: variable keyword arguments

A parameter prefixed with `**` collects any **extra keyword arguments** into a **dict**:

```python
def show(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

show(a=1, b=2)     # a = 1 / b = 2
show()             # nothing: kwargs is {}
```

The names `args` and `kwargs` are conventions. What matters is `*` and `**`.

### Combining parameter kinds

The order in a definition is: **regular positional → default → `*args` → keyword-only → `**kwargs`**.

```python
def f(a, b=2, *args, c, d=4, **kwargs):
    print(a, b, args, c, d, kwargs)

f(1, c=3)                       # 1 2 () 3 4 {}
f(1, 5, 6, 7, c=3, e=9)         # 1 5 (6, 7) 3 4 {'e': 9}
f(1)                            # TypeError: f() missing 1 required keyword-only argument: 'c'
```

Parameters after `*args` (here `c` and `d`) are **keyword-only**: positional arguments can't reach them, because `*args` absorbs them all.

```python
def g(*args, sep):
    ...
g(1, 2, " ")                    # TypeError: g() missing 1 required keyword-only argument: 'sep'
g(1, 2, sep=" ")                # OK
```

### Unpacking at the call site *(beyond the syllabus)*

`*` and `**` also work in the opposite direction, when calling:

```python
def add3(a, b, c):
    return a + b + c

nums = [1, 2, 3]
add3(*nums)                     # 6    (the list is unpacked into positional args)
opts = {"a": 1, "b": 2, "c": 3}
add3(**opts)                    # 6    (the dict is unpacked into keyword args)
print(*nums)                    # 1 2 3
print(*nums, sep=",")           # 1,2,3
```

---

## Exam traps
- At the call site, positional arguments must come before keyword arguments, or you get a `SyntaxError`.
- In a definition, a parameter without a default can't follow one with a default (`SyntaxError`).
- "Got multiple values for argument" means a positional and a keyword argument targeted the same parameter.
- Mutable defaults persist between calls.
- Mutating an argument is visible to the caller; rebinding it isn't.
- `*args` is a tuple and `**kwargs` is a dict. Either can be empty.
- Parameters after `*args` are keyword-only.

## Key takeaways
- Positional arguments match by order, keyword arguments by name, and defaults fill the gaps.
- Use `*args` and `**kwargs` to accept any number of extra arguments.
- Arguments are passed as references to objects.
